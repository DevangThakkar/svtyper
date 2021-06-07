from setuptools import setup, find_packages

with open('svtyper/version.py') as f:
    exec(f.read())

setup(
    name='svtyper',
    version=__version__,
    description='Bayesian genotyper for structural variants',
    long_description_content_type='text/markdown',
    author=__author__,
    author_email='colbychiang@wustl.edu',
    license='MIT License',
    url='https://github.com/devangthakkar/svtyper',
    install_requires=[
        'pysam>=0.15.0',
        'numpy',
        'scipy',
        'cytoolz>=0.8.2',
    ],
    scripts=[
        'scripts/sv_classifier.py',
        'scripts/update_info.py',
        'scripts/vcf_allele_freq.py',
        'scripts/vcf_group_multiline.py',
        'scripts/vcf_modify_header.py',
        'scripts/vcf_paste.py',
        'scripts/lib_stats.R',
    ],
    entry_points='''
        [console_scripts]
        svtyper=svtyper.classic:cli
        svtyper-sso=svtyper.singlesample:cli
    ''',
    packages=find_packages(exclude=('tests', 'etc')),
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)

