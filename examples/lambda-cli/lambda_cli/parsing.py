#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.04.2018 18:59
:Licence GPLv3
Part of lambda-cli

"""
from grammpy.transforms import ContextFree, InverseContextFree, InverseCommon
from grammpy.parsers import cyk
from .lambda_grammar import lambda_grammar
from .lex import lambda_cli_lex


_g = ContextFree.prepare_for_cyk(lambda_grammar)


def parse_from_tokens(input):
    parsed = cyk(_g, input)
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
