#!/usr/bin/env python
# coding=utf-8
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Anything you want',
    ext_modules=cythonize(["../libs/A/*.py", "../libs/B/*.py"
                            ], language_level=3
        ),
)
