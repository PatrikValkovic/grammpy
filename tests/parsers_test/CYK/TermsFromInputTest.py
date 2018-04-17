#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.03.2018 11:10
:Licence GNUv3
Part of pyparsers

"""

from unittest import main, TestCase

from grammpy import *
from grammpy.transforms import Traversing, ContextFree
from grammpy.parsers import cyk


class S(Nonterminal): pass
class X(Nonterminal): pass

class My:
    def __init__(self, prop):
        self.prop = prop
    def __hash__(self):
        return hash(My)


class R(Rule):
    rules = [
        ([S], [X]),
        ([X], [My]),
        ([X], [My, X])
    ]


class TermsFromInputTest(TestCase):

    def setUp(self):
        self.g = Grammar(terminals=[My],
                         nonterminals=[S, X],
                         rules=[R],
                         start_symbol=S)
        ContextFree.remove_useless_symbols(self.g, transform_grammar=True)
        ContextFree.remove_rules_with_epsilon(self.g, transform_grammar=True)
        ContextFree.remove_unit_rules(self.g, transform_grammar=True)
        ContextFree.remove_useless_symbols(self.g, transform_grammar=True)
        ContextFree.transform_to_chomsky_normal_form(self.g, transform_grammar=True)

    def test_oneTerminal(self):
        result = cyk(self.g, [My(1)])
        terms = filter(lambda x: isinstance(x, Terminal), Traversing.postOrder(result))
        terms = list(terms)
        self.assertEqual(terms[0].s.prop, 1)


    def test_twoTerminals(self):
        result = cyk(self.g, [My(1), My(2)])
        terms = filter(lambda x: isinstance(x, Terminal), Traversing.postOrder(result))
        terms = list(terms)
        self.assertEqual(terms[0].s.prop, 1)
        self.assertEqual(terms[1].s.prop, 2)

    def test_fiveTerminals(self):
        result = cyk(self.g, [My(1), My(2), My(3), My(4), My(5)])
        terms = filter(lambda x: isinstance(x, Terminal), Traversing.postOrder(result))
        terms = list(terms)
        self.assertEqual(terms[0].s.prop, 1)
        self.assertEqual(terms[1].s.prop, 2)
        self.assertEqual(terms[2].s.prop, 3)
        self.assertEqual(terms[3].s.prop, 4)
        self.assertEqual(terms[4].s.prop, 5)


if __name__ == '__main__':
    main()
