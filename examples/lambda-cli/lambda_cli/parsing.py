#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.04.2018 18:59
:Licence GPLv3
Part of lambda-cli

"""

from grammpy_transforms import ContextFree, InverseContextFree, InverseCommon
from pyparsers import cyk
from .lambda_grammar import lambda_grammar
from .lex import lambda_cli_lex
from .exceptions import ParsingException


_g = ContextFree.remove_useless_symbols(lambda_grammar)
_g = ContextFree.remove_rules_with_epsilon(_g, transform_grammar=True)
_g = ContextFree.remove_unit_rules(_g, transform_grammar=True)
_g = ContextFree.remove_useless_symbols(_g, transform_grammar=True)
_g = ContextFree.transform_to_chomsky_normal_form(_g, transform_grammar=True)


def parse_from_tokens(input):
    try:
        parsed = cyk(_g, input)
    except NotImplementedError:
        raise ParsingException
    parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
    parsed = InverseContextFree.unit_rules_restore(parsed)
    parsed = InverseContextFree.epsilon_rules_restore(parsed)
    parsed = InverseCommon.splitted_rules(parsed)
    return parsed.get_representation()

def parse(input):
    return parse_from_tokens(lambda_cli_lex(input))

def steps(input):
    repr = parse(input)
    yield repr.representation()
    while repr.beta_reduction():
        yield repr.representation()
