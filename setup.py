from setuptools import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
    CYTHON = True
except:
    CYTHON = False

DEPENDENCIES = ['setuptools']

# get the version without an import
VERSION = "Undefined"
DOC = ""
inside_doc = False
for line in open('vcf/__init__.py'):
    if "'''" in line:
        inside_doc = not inside_doc
    if inside_doc:
        DOC += line.replace("'''", "")

    if (line.startswith('VERSION')):
        exec(line.strip())

extras = {}
if CYTHON:
    extras['cmdclass'] = {'build_ext': build_ext}
    extras['ext_modules'] = [Extension("vcf.cparse", ["vcf/cparse.pyx"])]

setup(
    name='PyVCF',
    packages=['vcf', 'vcf.test'],
    scripts=['scripts/vcf_melt', 'scripts/vcf_filter.py',
             'scripts/vcf_sample_filter.py'],
    author='James Casbon and @jdoughertyii',
    author_email='casbon@gmail.com',
    description='Variant Call Format (VCF) parser for Python',
    long_description=DOC,
    test_suite='vcf.test.test_vcf.suite',
    install_requires=DEPENDENCIES,
    entry_points = {
        'vcf.filters': [
            'site_quality = vcf.filters:SiteQuality',
            'vgq = vcf.filters:VariantGenotypeQuality',
            'eb = vcf.filters:ErrorBiasFilter',
            'dps = vcf.filters:DepthPerSample',
            'avg-dps = vcf.filters:AvgDepthPerSample',
            'snp-only = vcf.filters:SnpOnly',
        ]
    },
    url='https://github.com/scwatts/PyVCF',
    version=VERSION,
    license='BSD/MIT',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
      ],
    keywords='bioinformatics',
    include_package_data=True,
    package_data = {
        '': ['*.vcf', '*.gz', '*.tbi'],
        },
    **extras
)
