import argparse

CBOLD = '\33[1m'
CEND = '\33[0m'
CRED = '\33[31m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'

def get_parser():
    parser = argparse.ArgumentParser(
        prog="sragetter",
        description='Tool for download the Sequencing Reads Archive data through ENA by using aspera',
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=f"""
{CBOLD}Usage{CEND}
-----------------
Download with one accession:
    {CRED}$ {CGREEN}sragetter{CEND} {CYELLOW}--accession{CEND} sra_accession {CYELLOW}--ssh-key{CEND} sshkey_path.ssh {CYELLOW}--outdir{CEND} outdir_path 

Download with TXT file containing multiple accessions:
    {CRED}$ {CGREEN}sragetter{CEND} {CYELLOW}--file{CEND} sra_accessions.txt {CYELLOW}--ssh-key{CEND} sshkey_path.ssh {CYELLOW}--outdir{CEND} outdir_path

Runjia Ji, 2023
"""
    )

    parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.2', help='Show SRAdownloader version number and exit')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-acc', '--accession', type=str, help='SRA data accession')
    group.add_argument('-f', '--file', type=str, help='TXT file with multiple SRA accessions')
    parser.add_argument('-ssh', '--ssh-key', dest='ssh_key', type=str, help="Public key authentication file provided by Aspera command line client download package as the 'asperaweb_id_dsa.openssh' file", required=True)
    parser.add_argument('-o', '--outdir', type=str, help='Path to store the downloaded SRA data', required=True)
    args = parser.parse_args()
    return args
