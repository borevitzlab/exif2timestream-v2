from distutils.core import setup
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
setup(
    name='exif2timestream-v2',
    version='0.9',
    python_requires='>=3.2',
    packages=['libexif2timestream2'],
    url='https://borevitzlab.github.io/exif2timestream-v2/',
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
    scripts=["exif2timestream-batch", 'exif2timestream-cli'],
    install_requires=requirements
)
