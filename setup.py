#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-pluginlu',
    version='1.0.0',
    author='Lucia Mejia',
    author_email='luquiceno@gmail.com',
    maintainer='Lucia Mejia',
    maintainer_email='luquiceno@gmail.com',
    license='GNU GPL v3.0',
    url='https://github.com/luquiceno/pytest-pluginlu',
    description='new reusable pytest plugin',
    long_description=read('README.rst'),
    py_modules=['pytest_pluginlutest'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    entry_points={
        'pytest11': [
            'pluginlu = pytest_pluginlutest',
        ],
    },
)
