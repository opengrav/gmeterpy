#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name='gmeterpy',
    description="Processing gravity measurements with Python",
    long_description=readme,
    license="MIT license",
    author="Ilya Oshchepkov",
    author_email='ilya@geod.ru',
    classifiers=[
        'Development Status :: 1 - Development',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
    ],
    keywords=['geodesy', 'gravimetry', 'geophysics'],
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['gmeterpy']),
    url='https://github.com/opengrav/gmeterpy',
    version='0.0.1',
    zip_safe=False,
)
