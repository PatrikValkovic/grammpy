#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 15:44
:Licence GNUv3
Part of lambda-cli

"""

from unittest import TestCase, main
from grammpy_transforms import ContextFree
from pyparsers import cyk
from lambda_cli import lambda_grammar, lambda_cli_lex


class FromAlphaReductionTest(TestCase):
    def setUp(self):
        self.g = lambda_grammar
        self.g = ContextFree.remove_useless_symbols(self.g)
        self.g = ContextFree.remove_rules_with_epsilon(self.g, transform_grammar=True)
        self.g = ContextFree.remove_unit_rules(self.g, transform_grammar=True)
        self.g = ContextFree.remove_useless_symbols(self.g, transform_grammar=True)
        self.g = ContextFree.transform_to_chomsky_normal_form(self.g, transform_grammar=True)

    def test_001(self):
        cyk(self.g, lambda_cli_lex("((lambda x y. (x y)) y)"))

    def test_002(self):
        cyk(self.g, lambda_cli_lex("(lambda y'. (y y'))"))

    def test_003(self):
        cyk(self.g, lambda_cli_lex("((lambda x. (lambda z. (x z))) (z g))"))

    def test_004(self):
        cyk(self.g, lambda_cli_lex("(lambda z'. ((z g) z'))"))

    def test_005(self):
        cyk(self.g, lambda_cli_lex("((lambda y. (lambda z. (z y))) y z)"))

    def test_006(self):
        cyk(self.g, lambda_cli_lex("(z y)"))

    def test_007(self):
        cyk(self.g, lambda_cli_lex("((lambda x. (lambda y. (y (lambda x. x) x))) x)"))

    def test_008(self):
        cyk(self.g, lambda_cli_lex("(lambda y. (y (lambda x'. x') x))"))


if __name__ == '__main__':
    main()
