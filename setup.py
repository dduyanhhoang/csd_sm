# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Student manager - SUM2024 CSD203 Lab 1 ',
    long_description=readme,
    author='Hoang Dinh Duy Anh',
    author_email='dduyanhhoang@gmail.cm',
    url='https://github.com/dduyanhhoang',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

