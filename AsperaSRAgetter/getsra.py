from .getparser import get_parser
import requests
from io import StringIO
import pandas as pd
import math
import os
import logging

logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt="%H:%M:%S"
    )

def dl(acc, sshkey, outdir):
    _s=acc.center(16)
    print(
        f"""
####################
##{_s}##
####################
"""
    )
    if os.path.isdir(outdir):
        logging.info(f"SRA data will be downloaded into {outdir}")
    else:
        logging.critical('An error occurred. Please see the info below')
        raise Exception(f'Sorry, the {outdir} does not exists. Please pass a exist folder to store the SRA data.')
    
    log_file = os.path.join(outdir,'download_records.tsv')
    base_url = 'era-fasp@fasp.sra.ebi.ac.uk:'

    headers = {
        'accept': '*/*',
    }

    params = {
        'accession': acc,
        'result': 'read_run',
    }

    # Getting the accession report and write out to TSV file
    logging.info(f"{acc} file report is being retrieved from ENA using ENA filereport api")
    response = requests.get('https://www.ebi.ac.uk/ena/portal/api/filereport', params=params, headers=headers)
    record = pd.read_csv(StringIO(response.text), sep='\t')
    record['datetime'] = pd.Timestamp.now()

    logging.info(f"Writing {acc} report to download_records.tsv file")
    if not os.path.isfile(log_file):
        record.to_csv(log_file, index=False, sep='\t')
    else:
        records = pd.read_csv(log_file, sep='\t')
        records = pd.concat([records, record])
        records = records.drop_duplicates(subset=['run_accession'], keep='last')
        records.to_csv(log_file, index=False, sep='\t')

    # Getting the fastq ftp urls for Aspera to download fastqs
    fastq_ftp = record.loc[0, 'fastq_ftp']
    if isinstance(fastq_ftp,str):
        fq_urls = fastq_ftp.split(';')
    elif math.isnan(fastq_ftp):# If no fastq ftq urls, warning the user and abort this download
        logging.warning('No fastq ftp url was found')
        logging.warning(f'Downloading aborted. Writing {acc} to failed.txt')
        failed_file = open(os.path.join(outdir, 'failed.txt'), 'a', encoding='utf-8')
        failed_file.write(f'{acc}\n')
        failed_file.close()
        return
    
    md5_value = record.loc[0, 'fastq_md5']
    md5s = md5_value.split(';')

    # Download fastqs and record md5sum hash values
    md5_file = open(os.path.join(outdir, 'fastq.md5'), 'a', encoding='utf-8')
    for _url, md5 in zip(fq_urls, md5s):
        url = base_url + _url.lstrip('ftp.sra.ebi.ac.uk/')
        cmd = f'ascp -QT -l 300m -P 33001 -i "{sshkey}" "{url}" "{outdir}"'
        logging.info(f'Command is: {cmd}')
        logging.info('Downloading has started...')
        return_code = os.system(cmd)
        filename = _url.split('/')[-1]
        if return_code == 0:
            logging.info(f"Writing {filename} md5 hash value to fastq.md5 file")
            md5_file.write(f'{md5}\t{filename}\n')
        else:
            logging.info(f'Something went wrong when downloading {filename}')
            logging.info(f'{filename} downloading failed. Writing {filename} to failed.txt')
            failed_file = open(os.path.join(outdir, 'failed.txt'), 'a', encoding='utf-8')
            failed_file.write(f'{filename}\n')
            failed_file.close()
    logging.info(f'{acc} data successfully downloaded')
    md5_file.close()
    
