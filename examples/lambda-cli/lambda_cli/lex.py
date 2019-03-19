#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 16:42
:Licence GPLv3
Part of lambda-cli

"""
from ply import lex
from .exceptions import LexException
from .terminals import *

states = (
    ('parameters', 'exclusive'),
)

tokens = (
    'LAMBDA',
    'DOT',
    'NUMBER',
    'VARIABLE',
    'PARAMETER',
    'LEFTBRACKET',
    'RIGHTBRACKET',
)

t_INITIAL_parameters_ignore = ' \t'


def t_INITIAL_LAMBDA(t):
    r'lambda'
    t.value = LambdaKeyword
    t.lexer.begin('parameters')
    return t


def t_parameters_DOT(t):
    r'\.'
    t.value = Dot
    t.lexer.begin('INITIAL')
    return t


def t_INITIAL_NUMBER(t):
    r'\d+'
    t.value = Number(int(t.value))
    return t


def t_INITIAL_VARIABLE(t):
    r'[a-zA-Z\']+'
    t.value = Variable(t.value)
    return t


def t_parameters_PARAMETER(t):
    r'[a-zA-Z\']+'
    t.value = Parameter(t.value)
    return t


def t_INITIAL_LEFTBRACKET(t):
    r'\('
    t.value = LeftBracket
    return t


def t_INITIAL_RIGHTBRACKET(t):
    r'\)'
    t.value = RightBracket
    return t

def t_INITIAL_parameters_error(t):
    raise LexException(t)

lexer = lex.lex()


def lambda_cli_lex(input):
    lexer.input(input)
    while True:
        tok = lexer.token()
        if not tok:
            return  # No more input
        yield tok.value
