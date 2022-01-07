import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

setup(
    name='financial_system',
    version='0.0',
    description='Financial System',
    packages=find_packages(),
    entry_points={
        'paste.app_factory': [
            'main = financial_system:main',
        ],
    },
)
