#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.08.2017 19:00
:Licence GNUv3
Part of grammpy

"""


from setuptools import setup

v = '1.2.4'

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
        'grammpy.representation.grammars',
        'grammpy.representation.rules',
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
    license='GNU General Public License v3.0',
    author='Patrik Valkovic',
    author_email='patrik.valkovic@hotmail.cz',
    description='CYK library with all required tools to parse context-free grammars.',
    install_requires=[
        'typing',
    ],
)
