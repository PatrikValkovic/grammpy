#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 30.03.2018 16:35
:Licence GNUv3
Part of pyparsers

"""

from unittest import main, TestCase
from grammpy import *
from pyparsers import cyk
from grammpy_transforms import ContextFree, InverseContextFree


class S(Nonterminal): pass
class My:
    def __init__(self, prop):
        self.prop = prop
    def __hash__(self):
        return hash(My)


class R(Rule):
    rule = (
        [S],
        [My, My]
    )



class CorrectTerminalsTest(TestCase):

    def setUp(self):
        self.g = Grammar(terminals=[My],
                         nonterminals=[S],
                         rules=[R],
                         start_symbol=S)
        ContextFree.remove_useless_symbols(self.g, transform_grammar=True)
        ContextFree.remove_rules_with_epsilon(self.g, transform_grammar=True)
        ContextFree.remove_unit_rules(self.g, transform_grammar=True)
        ContextFree.remove_useless_symbols(self.g, transform_grammar=True)
        ContextFree.transform_to_chomsky_normal_form(self.g, transform_grammar=True)


    def test_sameHashes(self):
        self.assertEqual(hash(My), hash(My(1)))

    def test_shouldParseClass(self):
        parsed = cyk(self.g, [My, My])

    def test_shouldParseInstances(self):
        parsed = cyk(self.g, [My(1), My(2)])

    def test_shouldParseAndUseValues(self):
        parsed = cyk(self.g, [My(1), My(2)])
        parsed = InverseContextFree.transform_from_chomsky_normal_form(parsed)
        parsed = InverseContextFree.unit_rules_restore(parsed)
        parsed = InverseContextFree.epsilon_rules_restore(parsed)

        self.assertIsInstance(parsed, S)
        self.assertIsInstance(parsed.to_rule, R)
        left = parsed.to_rule.to_symbols[0]
        right = parsed.to_rule.to_symbols[1]
        self.assertIsInstance(left, Terminal)
        self.assertIsInstance(left.s, My)
        self.assertEqual(left.s.prop, 1)
        self.assertIsInstance(right, Terminal)
        self.assertIsInstance(right.s, My)
        self.assertEqual(right.s.prop, 2)


if __name__ == '__main__':
    main()

