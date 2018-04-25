### stx_subtyping: a tool for subtyping shiga toxin genes from fastqs or fastas.

## NOTE: I have cloned this from https://github.com/flashton2003/stx_subtyping

**Installation**

pip install git+https://github.com/AdmiralenOla/stx_subtyping

**Requirements**

Tested with Biopython v1.6.3
Test with pysam v0.6
Bowtie2
Need to have bowtie2 installed and available in your PATH (i.e. when you type `bowtie2` from any location, it runs bowtie2)

**Useage**

stx_subtyping -h
stx_subtyping dual_stx_subtyping -h

stx_subtyping dual_stx_subtyping /path/to/fastq1.fastq /path/to/fastq2.fastq /path/to/contigs.fa /path/to/whereyouwanttheoutput

There are 3 running options. The best approach is dual_stx_subtyping, but if only fastqs or fastas are available, the other options can be used.

dual\_stx\_subtyping - Takes a pair of fastqs and a set of contigs for a strain, outputs info into output_dir

assblast_only - Use this when you only have contigs

mapsnp_only - Use this when you only have fastqs, no assemblies

If in doubt, try -h
