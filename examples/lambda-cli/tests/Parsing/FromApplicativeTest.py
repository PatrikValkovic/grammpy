#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.03.2018 18:32
:Licence GPLv3
Part of lambda-cli

"""



from unittest import TestCase, main
from grammpy_transforms import ContextFree
from pyparsers import cyk
from lambda_cli import lambda_grammar, lambda_cli_lex


class FromApplicativeTest(TestCase):
    def setUp(self):
        self.g = lambda_grammar
        self.g = ContextFree.remove_useless_symbols(self.g)
        self.g = ContextFree.remove_rules_with_epsilon(self.g, transform_grammar=True)
        self.g = ContextFree.remove_unit_rules(self.g, transform_grammar=True)
        self.g = ContextFree.remove_useless_symbols(self.g, transform_grammar=True)
        self.g = ContextFree.transform_to_chomsky_normal_form(self.g, transform_grammar=True)

    def test_001(self):
        cyk(self.g, lambda_cli_lex("((lambda x. x) (lambda y. y) (lambda z. z))"))

    def test_002(self):
        cyk(self.g, lambda_cli_lex("((lambda y. y) (lambda z. z))"))

    def test_003(self):
        cyk(self.g, lambda_cli_lex("(lambda x. ((lambda y. y) 2 x))"))

    def test_004(self):
        cyk(self.g, lambda_cli_lex("(x y (lambda x. ((lambda y. x) 3)))"))

    def test_005(self):
        cyk(self.g, lambda_cli_lex("((lambda x y. ((lambda z. ((lambda f. (z f)) z)) x)) 3 7)"))


if __name__ == '__main__':
    main()