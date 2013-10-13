#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
  import setuptools
  from setuptools import setup, find_packages
except ImportError:
  print("Please install setuptools.")

def find_scripts(scripts_path):
  base_path = os.path.abspath(scripts_path)
  return list(map(lambda path: os.path.join(scripts_path, path), 
           filter(lambda file_name: os.path.isfile(
             os.path.join(base_path, file_name)), os.listdir(base_path)
         )))

import os
import sys

libdir = "lib"
bindir = os.path.join(libdir, "bin")

sys.path.insert(0, libdir)

from fizzbuzz import __info__

setup_options = __info__
setup_options.update({
  "scripts": find_scripts(bindir),
  "packages": find_packages(libdir),
  "package_dir": {"": libdir},
})

setup(**setup_options)
