#!/usr/bin/env python3
import logging
import os

logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt="%H:%M:%S"
    )

def main():
    from .getparser import get_parser
    from .getsra import dl

    args = get_parser()
    acc = args.accession
    inputfile = args.file
    sshkey = args.ssh_key
    outdir = args.outdir
    if acc:
        dl(acc=acc, sshkey=sshkey, outdir=outdir)
    elif inputfile:
        if os.path.isfile(inputfile):
            logging.info(f'Input file is {inputfile}')
            with open(inputfile)as f:
                accs=[i.strip() for i in f.readlines()]
            for acc in accs:
                dl(acc=acc, sshkey=sshkey, outdir=outdir)
        else:
            logging.info(f'{inputfile} is not a file. Exiting...')
                
#############################################
if __name__ == '__main__':
    main()