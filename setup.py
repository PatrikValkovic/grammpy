#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.08.2017 19:00
:Licence MIT
Part of grammpy

"""
from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

v = '2.0.0'

setup(
    name='grammpy',
    version=v,
    packages=[
        'grammpy',
        'grammpy.exceptions',
        'grammpy.old_api',
        'grammpy.parsers',
        'grammpy.parsers.CYK',
        'grammpy.representation',
        'grammpy.representation.support',
        'grammpy.transforms',
        'grammpy.transforms.ChomskyForm',
        'grammpy.transforms.EpsilonRulesRemove',
        'grammpy.transforms.NongeneratingSymbolsRemove',
        'grammpy.transforms.SplittedRules',
        'grammpy.transforms.UnitRulesRemove',
        'grammpy.transforms.UnreachableSymbolsRemove',
    ],
    url='https://github.com/PatrikValkovic/grammpy',
    download_url='https://github.com/PatrikValkovic/grammpy/archive/v' + v + '.tar.gz',
    license='The MIT License',
    author='Patrik Valkovic',
    author_email='patrik.valkovic@hotmail.cz',
    description='CYK library with all required tools to parse context-free grammars.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'typing',
        'deprecated',
    ],
)
