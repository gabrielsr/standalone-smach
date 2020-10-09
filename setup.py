#!/usr/bin/env python

from setuptools import setup
import generate_distutils_setup

d = generate_distutils_setup(
   packages=['smach'],
   package_dir={'': 'src'}
)

setup(**d)
