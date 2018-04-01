#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.03.2018 18:32
:Licence GPLv3
Part of lambda-cli

"""



from unittest import TestCase, main
from grammpy_transforms import ContextFree, InverseCommon, InverseContextFree
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
        parsed = cyk(self.g, lambda_cli_lex("((lambda x. x) (lambda y. y) (lambda z. z))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_002(self):
        parsed = cyk(self.g, lambda_cli_lex("((lambda y. y) (lambda z. z))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_003(self):
        parsed = cyk(self.g, lambda_cli_lex("(lambda x. ((lambda y. y) 2 x))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_004(self):
        parsed = cyk(self.g, lambda_cli_lex("(x y (lambda x. ((lambda y. x) 3)))"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()

    def test_005(self):
        parsed = cyk(self.g, lambda_cli_lex("((lambda x y. ((lambda z. ((lambda f. (z f)) z)) x)) 3 7)"))
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)
        parsed = InverseCommon.splitted_rules(parsed)
        parsed.get_representation()



if __name__ == '__main__':
    main()