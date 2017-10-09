# from distutils.core import setup
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='exif2timestream',
    version='0.9',
    python_requires='>=3.2',
    packages=['libexif2timestream2'],
    url='https://borevitzlab.github.io/exif2timestream/',
    license='GPLv3',
    author='Gareth Dunstone, Borevitz Lab, Australian Plant Phenomics Facility',
    author_email='gareth.dunstone@anu.edu.au',
    description='A tool to turn unstructured timelapses into nested directory trees with downsampled images based on exif data.',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only"
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    keywords=['timelapse', 'imaging'],
    entry_points={
        'console_scripts': [
            'exif2timestream-batch=exif2timestream_batch.py',
            'exif2timestream-cli=exif2timestream_cli.py'
        ]
    },
    install_requires=requirements
)
