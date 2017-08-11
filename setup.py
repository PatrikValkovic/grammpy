#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.08.2017 19:00
:Licence GNUv3
Part of grammpy

"""

from distutils.core import setup


setup(
    name='grammpy',
    version='1.1.0',
    packages=['grammpy', 'grammpy.Grammars', 'grammpy.exceptions'],
    url='https://github.com/PatrikValkovic/grammpy',
    license='GNU General Public License v3.0',
    author='Patrik Valkovic',
    download_url='https://github.com/PatrikValkovic/grammpy/archive/v1.0.1.tar.gz',
    author_email='patrik.valkovic@hotmail.cz',
    description='Package for representing formal grammars.'
)
