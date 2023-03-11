# AsperaSRAgetter
AsperaSRAgetter provides a easy way to download sequencing data (fastq.gz format) from European Nucleotide Archive (ENA) by using Aspera.

## Installation
AsperaSRAgetter has been distributed on [pypi](https://pypi.org/project/AsperaSRAgetter/). You can easily install AsperaSRAgetter through pip. AsperaSRAgetter depends on Aspera-CLI to retrive sequencing data from ENA. [Conda](https://anaconda.org/hcc/aspera-cli) is recommended to install Aspera-CLI.
```bash
# You may create a new invironment for AsperaSRAgetter, but this is optional
conda create -n AsperaSRAgetter python=3.10
conda activate AsperaSRAgetter

# Install AsperaSRAgetter using pip
pip install AsperaSRAgetter

# Install Aspera-CLI using conda
conda install -c hcc aspera-cli
```

## Usage

The command name of AsperaSRAgetter is **sragetter**. It accepts either one SRA accession or one TXT file containing multiple accessions (see the usage example below). 
Note that users need to provide the path of public key authentication file of Aspera-CLI (normally should be ENVIRONMENT_PATH/etc/asperaweb_id_dsa.openssh)

```bash
usage: sragetter [-h] [-v] [-acc ACCESSION | -f FILE] -ssh SSH_KEY -o OUTDIR

options:
  -h, --help            show this help message and exit
  -v, --version         Show SRAdownloader version number and exit
  -acc ACCESSION, --accession ACCESSION
                        SRA data accession
  -f FILE, --file FILE  TXT file with multiple SRA accessions
  -ssh SSH_KEY, --ssh-key SSH_KEY
                        Public key authentication file provided by Aspera command line client download package as the 'asperaweb_id_dsa.openssh' file
  -o OUTDIR, --outdir OUTDIR
                        Path to store the downloaded SRA data

Usage
-----------------
Download with one accession:
    $ sragetter --accession sra_accession --ssh-key sshkey_path.openssh --outdir outdir_path

Download with TXT file containing multiple accessions:
    $ sragetter --file sra_accessions.txt --ssh-key sshkey_path.openssh --outdir outdir_path
```