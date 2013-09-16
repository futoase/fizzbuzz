#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
  import setuptools
  from setuptools import setup, find_packages
except ImportError:
  print("Please install setuptools.")

try:
  from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
  from distutils.command.build_py import build_py

import sys

libdir = "lib"
sys.path.insert(0, libdir)

import fizzbuzz as pkg

setup_options = {
  "scripts": ["lib/bin/fizzbuzz"],
  "name": pkg.__name__,
  "version": pkg.__version__,
  "description": pkg.__description__,
  "author": pkg.__author__,
  "author_email": pkg.__author_email__,
  "license": pkg.__license__,
  "url": pkg.__url__,
  "packages": find_packages(libdir),
  "package_dir": {"": libdir},
  "classifiers": pkg.__classifiers__
}

setup(**setup_options)
