#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 14.12.2024 14:31
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import create_ll_parsing_table, ll
from grammpy.transforms import *


class SimpleTableTest(TestCase):
    def test_disrepancyBetweenTableAndRules(self):
        class S(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S],
            rules=[SRule],
            start_symbol=S
        )
        parsing_table = {
            S: {
                (1,): {SRule}
            }
        }
        with self.assertRaises(Exception) as catched:
            ll(g.start, [1], parsing_table, 1)
        self.assertEqual(catched.exception.args[0], 'Expected terminal 0, but found 1')

    def test_invalidInput(self):
        class S(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0, S])
        class SRuleEps(Rule):
            rule = ([S], [EPSILON])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S],
            rules=[SRule, SRuleEps],
            start_symbol=S
        )
        first = ContextFree.create_first_table(g, 1)
        follow = ContextFree.create_follow_table(g, first, 1)
        table = create_ll_parsing_table(g, first, follow, 1)
        with self.assertRaises(Exception) as catched:
            ll(g.start, [0, 0, 0, 1,0], table, 1)
        self.assertEqual(catched.exception.args[0], 'Rule for S with lookahead (1,) not found')

    def test_missingNonterminalInParsingTable(self):
        class S(Nonterminal): pass
        class A(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0, A])
        class ARule(Rule):
            rule = ([A], [1])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S, A],
            rules=[SRule, ARule],
            start_symbol=S
        )
        parsing_table = {
            S: {
                (0,): {SRule}
            }
        }
        with self.assertRaises(Exception) as catched:
            ll(g.start, [0, 1], parsing_table, 1)
        self.assertEqual(catched.exception.args[0], 'There is no rules for nonterminal A')

    def test_missingLookAhead(self):
        class S(Nonterminal): pass
        class A(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0, A])
        class ARule(Rule):
            rule = ([A], [1])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S, A],
            rules=[SRule, ARule],
            start_symbol=S
        )
        parsing_table = {
            S: {
                (0,): {SRule}
            },
            A: {}
        }
        with self.assertRaises(Exception) as catched:
            ll(g.start, [0, 1], parsing_table, 1)
        self.assertEqual(catched.exception.args[0], 'Rule for A with lookahead (1,) not found')

    def test_emptyRuleSet(self):
        class S(Nonterminal): pass
        class A(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0, A])
        class ARule(Rule):
            rule = ([A], [1])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S, A],
            rules=[SRule, ARule],
            start_symbol=S
        )
        parsing_table = {
            S: {
                (0,): {SRule}
            },
            A: {
                (1,): set()
            }
        }
        with self.assertRaises(Exception) as catched:
            ll(g.start, [0, 1], parsing_table, 1)
        self.assertEqual(catched.exception.args[0], 'No rule to apply for A with lookahead (1,)')

    def test_tableWithAmbiguity(self):
        class S(Nonterminal): pass
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0, A])
        class SRule2(Rule):
            rule = ([S], [0, B])
        class ARule(Rule):
            rule = ([A], [1])
        class BRule(Rule):
            rule = ([B], [1])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S, A, B],
            rules=[SRule, ARule, SRule2, BRule],
            start_symbol=S
        )
        first = ContextFree.create_first_table(g, 1)
        follow = ContextFree.create_follow_table(g, first, 1)
        table = create_ll_parsing_table(g, first, follow, 1)
        with self.assertRaises(Exception) as catched:
            ll(g.start, [0, 1], table, 1)
        self.assertEqual(catched.exception.args[0], 'Ambiguity found for S with lookahead (0,)')

    def test_tableWithIgnoredAmbiguity(self):
        class S(Nonterminal): pass
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0, A])
        class SRule2(Rule):
            rule = ([S], [0, B])
        class ARule(Rule):
            rule = ([A], [1])
        class BRule(Rule):
            rule = ([B], [1])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S, A, B],
            rules=[SRule, ARule, SRule2, BRule],
            start_symbol=S
        )
        first = ContextFree.create_first_table(g, 1)
        follow = ContextFree.create_follow_table(g, first, 1)
        table = create_ll_parsing_table(g, first, follow, 1)
        ll(g.start, [0, 1], table, 1, raise_on_ambiguity=False)

    def test_parsingTableWithoutRule(self):
        class S(Nonterminal): pass
        class SRule(Rule):
            rule = ([S], [0])
        g = Grammar(
            terminals=[0, 1],
            nonterminals=[S],
            rules=[SRule],
            start_symbol=S
        )
        parsing_table = {
            S: {
                (0,): {'not a rule'}
            }
        }
        with self.assertRaises(Exception) as catched:
            ll(g.start, [0], parsing_table, 1)
        self.assertEqual(catched.exception.args[0], 'Rule is not subclass of Rule')

if __name__ == '__main__':
    main()
