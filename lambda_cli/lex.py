#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 16:42
:Licence GNUv3
Part of lambda-cli

"""

from .terminals import *

def _right(rest):
    symb = 'x'
    while symb is not '.':
        parameter_name = None
        while not symb.isspace():
            symb
            parameter_name += symb
    yield Dot

def _left(rest):
    symb = next(rest)
    if symb is '(' or symb is ')':
        yield symb




def lambda_cli_lex(input):
    input = (s for s in input)
    return _left(input)