#!
# -*- coding: utf-8 -*-
"""
Created on  Jun 13, 2020

@author: Vikram Khaire
"""

from setuptools import setup, find_packages, Extension
import numpy as np


setup(name='astrodata',
      version='0.1',
      description='For accessing small published data tables in Astronomy',
      author='Vikram Khaire',
      author_email='vickykhaire@gmail.com',
      url='https://github.com/vikramkhaire/astrodata',
      packages=find_packages(include=['*.py','*.c','*.h']),
      include_dirs=np.get_include(),
      install_requires=['astropy',
                        'scipy',
                        'numpy',
                        'matplotlib'],
     )
