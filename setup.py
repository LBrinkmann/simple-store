from setuptools import setup, find_packages
import sys
import os.path


def load_requirements():
    with open('requirements.txt') as f:
        lines = f.readlines()
    return lines


setup(name='sstore',
      version="0.0.1",
      description='',
      url='',
      author='Levin Brinkmann',
      author_email='',
      license='',
      packages=['smart_open', 'pandas', 'numpy'],
      zip_safe=False,
      install_requires=load_requirements(),
      extras_require={},
      package_data={},
      scripts=[]
      )
