<<<<<<< HEAD
#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.08.2017 19:00
:Licence GNUv3
Part of grammpy

"""

from setuptools import setup

v = '1.2.1'
setup(
    name='grammpy',
    version=v,
    packages=['grammpy', 'grammpy.Grammars', 'grammpy.exceptions', 'grammpy.Rules'],
    url='https://github.com/PatrikValkovic/grammpy',
    license='GNU General Public License v3.0',
    author='Patrik Valkovic',
    download_url='https://github.com/PatrikValkovic/grammpy/archive/v' + v + '.tar.gz',
    author_email='patrik.valkovic@hotmail.cz',
    description='Package for representing formal grammars.',
    install_requires=[
        'typing'
=======
from setuptools import setup

v = '1.2.4'

setup(
    name='grammpy-transforms',
    version=v,
    packages=[
        'grammpy_transforms',
        'grammpy_transforms.ChomskyForm',
        'grammpy_transforms.UnitRulesRemove',
        'grammpy_transforms.EpsilonRulesRemove',
        'grammpy_transforms.UnreachableSymbolsRemove',
        'grammpy_transforms.NongeneratingSymbolsRemove',
        'grammpy_transforms.SplittedRules'
    ],
    url='https://github.com/PatrikValkovic/grammpy-transforms',
    download_url='https://github.com/PatrikValkovic/grammpy-transforms/archive/v' + v + '.tar.gz',
    license='GNU General Public License v3.0',
    author='Patrik Valkovic',
    author_email='patrik.valkovic@hotmail.cz',
    description='Set of transformations for grammpy library.',
    install_requires=[
        'grammpy',
>>>>>>> transforms/master
    ],
)
