#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


# Add your dependencies here
install_requires = ['pluggy', 'imageio', 'numpy']

install_requires += ['napari>=0.2.12'],


setup(
    name='napari-io-test',
    version='0.0.1',
    author='Nicholas Sofroniew',
    author_email='sofroniewn@gmail.com',
    maintainer='Nicholas Sofroniew',
    maintainer_email='sofroniewn@gmail.com',
    license='BSD-3',
    url='https://github.com/sofroniewn/napari-io-test',
    description='A napari IO test plugin',
    long_description=read('README.rst'),
    py_modules=['napari_io_test'],
    python_requires='>=3.6',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'napari.plugin': [
            'io-test = napari_io_test',
        ],
    },
)
