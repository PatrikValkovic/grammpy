#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 16:42
:Licence GNUv3
Part of lambda-cli

"""

from ply import lex
from .terminals import *


def lambda_cli_lex(input):
    return input