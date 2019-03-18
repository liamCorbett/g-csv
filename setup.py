from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gcsv',
    version='0.1.0',
    author='Liam Corbett',
    description='A tool for dealing with csv files and Google Sheets.',
    long_description=long_description,
    url='https://github.com/liamCorbett/gcsv',
    keywords='',
    py_modules=['gcsv'],
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
    ]
)