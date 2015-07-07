from setuptools import setup, find_packages

setup(
    name = 'pycronally',
    version = '0.1',
    py_modules = ['pycronally'],
    author = 'Cronally Team',
    author_email = 'team@cronally.com',
    description = 'Cronally Python client library',
    keywords = 'cronally, cronjobs, aws cronjobs',
    url = 'https://cronally.com',
    install_requires = ['requests']
)