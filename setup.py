from setuptools import setup
from distutils.util import convert_path

versionholder = {}
ver_path = convert_path('stx_subtyping/__init__.py')
with open(ver_path) as init_file:
    exec(init_file.read(), versionholder)

setup(name='stx_subtyping',
    version=versionholder['__version__'],
    description='Subtyping of the stx genes of Escherichia coli using raw (FASTQ) data and contigs (FASTA).',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    keywords=['stx','Ecoli','Escherichia','coli','typing','shiga','shigatoxin','verotoxin'],
    author=['Ola Brynildsrud','Philip Ashton'],
    author_email='ola.brynildsrud@fhi.no',
    packages=['stx_subtyping'],
    install_requires=[
        'biopython',
        'pysam'],
    entry_points={
        'console_scripts': ['stx_subtyping=stx_subtyping.stx_subtyping:main']
    },
    package_data={'stx_subtyping': ['setup.py', 'stx_subtyping/refs/*']},
    include_package_data=True
)