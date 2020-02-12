from setuptools import setup, find_packages
import sys
import os.path

PACKAGE_NAME = 'sstore'


setup(name=PACKAGE_NAME,
      version="0.0.1",
      description='',
      url='',
      author='Levin Brinkmann',
      author_email='',
      license='',
      packages=[package for package in find_packages()
                if package.startswith(PACKAGE_NAME)],
      zip_safe=False,
      install_requires=['wheel', 'smart_open', 'pandas', 'numpy'],
      extras_require={},
      package_data={},
      scripts=[]
      )
