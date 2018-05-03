#################################### imports ####################################

import sys, os, pysam
from os import system
from datetime import datetime
import argparse

from .__init__ import __version__

#################################### functions ####################################

def run_command(args):
	if args.command == 'dual_stx_subtyping':
		make_output_dir(args.output_root)
		run_MapSNP(args.fastq1, args.fastq2, args.output_root)
		run_AssBLAST(args.contigs, args.output_root)

	if args.command == 'assblast_only':
		make_output_dir(args.output_root)
		run_AssBLAST(args.contigs, args.output_root)

	if args.command == 'mapsnp_only':
		make_output_dir(args.output_root)
		run_MapSNP(args.fastq1, args.fastq2, args.output_root)

def make_output_dir(output_root):
	if not os.path.isdir(output_root):
		system ('mkdir %s' % output_root)
	if not os.path.isdir('%s/tmp' % output_root):
		system ('mkdir %s/tmp' % output_root)

def get_scripts_dir():
	return os.path.dirname(os.path.realpath(__file__))

def get_ref_fasta():
	scripts_dir = os.path.dirname(os.path.realpath(__file__))
	ref = '%s/refs/stx_genes_with_flanking_regions.fa' % scripts_dir
	return ref

def run_MapSNP(fastq_read1, fastq_read2, output_root):
	scripts_dir = get_scripts_dir()
	ref = get_ref_fasta()
	print('###  START:' + str(datetime.time(datetime.now())).split('.')[0])
	print('###  Running MapSNP workflow...' + str(datetime.time(datetime.now())).split('.')[0])
	system ('python %s/run_MapSNP.py %s %s %s %s' % (scripts_dir, fastq_read1, fastq_read2, output_root, ref))
	
def run_AssBLAST(contigs, output_root):
	scripts_dir = get_scripts_dir()
	ref = get_ref_fasta()
	print('### START:' + str(datetime.time(datetime.now())).split('.')[0])
	print('###  Running AssBLAST workflow...' + str(datetime.time(datetime.now())).split('.')[0])
	system ('python %s/run_AssBLAST.py %s %s %s' % (scripts_dir, contigs, output_root, ref))

#################################### main ####################################



def main():
	parser = argparse.ArgumentParser(prog='stx_subtyping')
	parser.add_argument("-v", "--version", help="Installed stx_subtyping version", action="version",
                        version="%(prog)s " + str(__version__))
	subparsers = parser.add_subparsers(title='[sub-commands]', dest='command')
	parser_dual_stx_subtyping = subparsers.add_parser('dual_stx_subtyping', help='Takes a pair of fastqs and a set of contigs for a strain, outputs info into output_dir')
	parser_dual_stx_subtyping.add_argument('fastq1', help = 'Fastq 1')
	parser_dual_stx_subtyping.add_argument('fastq2', help = 'Fastq 2')
	parser_dual_stx_subtyping.add_argument('contigs', help = 'Contigs')
	parser_dual_stx_subtyping.add_argument('output_root', help = 'Directory into which you want the output')

	parser_assblast_only = subparsers.add_parser('assblast_only', help ='Use this when you only have contigs')
	parser_assblast_only.add_argument('contigs', help = 'Contigs')
	parser_assblast_only.add_argument('output_root', help = 'Directory into which you want the output')

	parser_mapsnp_only = subparsers.add_parser('mapsnp_only', help = 'Use this when you only have fastqs, no assemblies')
	parser_mapsnp_only.add_argument('-1', dest = 'fastq1', help = 'Fastq 1')
	parser_mapsnp_only.add_argument('-2', dest = 'fastq2', help = 'Fastq 2')
	parser_mapsnp_only.add_argument('output_root', help = 'Directory into which you want the output')
	args = parser.parse_args()
	run_command(args)


if __name__ == '__main__':
	main()