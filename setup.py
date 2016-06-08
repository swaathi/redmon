# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='redmon',
    version='0.0.1',
    description='Monitor a Redis key',
    long_description=readme,
    author=['Swaathi Kakarla'],
    author_email=['swaathi@skcript.com'],
    url='http://www.skcript.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'redmon = redmon.cli:main',
        ],
    },
    install_requires=(
    	['redis'], ['click'], ['pytest']
    )
)
