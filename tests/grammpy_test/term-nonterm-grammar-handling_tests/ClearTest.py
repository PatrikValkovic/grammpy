#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy.old_api import *


class First(Nonterminal): pass
class Second(Nonterminal): pass
class Third(Nonterminal): pass

class FirstR(Rule):
    rule = ([First], [First, First])
class SecondR(Rule):
    rule = ([Second], [First, First])
class ThirdR(Rule):
    rule = ([Third], [First, First])


class ClearTest(TestCase):

    def test_clearTerminals(self):
        g = Grammar(terminals='0123')
        self.assertEqual(g.terms_count(), 4)
        g.terms_clear()
        self.assertEqual(g.terms_count(), 0)
        g.add_term('0')
        self.assertEqual(g.terms_count(), 1)
        g.terms_clear()
        self.assertEqual(g.terms_count(), 0)

    def test_clearTerminalsReturnValue(self):
        g = Grammar(terminals='0123')
        deleted = g.terms_clear()
        self.assertEqual(len(deleted), 4)
        for ch in '0123':
            self.assertIn(ch, [t.s for t in deleted])
        g.add_term('0')
        deleted = g.terms_clear()
        self.assertEqual(len(deleted), 1)
        self.assertIn('0', [t.s for t in deleted])


    def test_clearNonterminals(self):
        g = Grammar(nonterminals=[First, Second, Third])
        self.assertEqual(g.nonterms_count(), 3)
        g.nonterms_clear()
        self.assertEqual(g.nonterms_count(), 0)
        g.add_nonterm(First)
        self.assertEqual(g.nonterms_count(), 1)
        g.nonterms_clear()
        self.assertEqual(g.nonterms_count(), 0)

    def test_clearNonterminalsReturnValue(self):
        g = Grammar(nonterminals=[First, Second, Third])
        deleted = g.nonterms_clear()
        self.assertEqual(len(deleted), 3)
        for n in [First, Second, Third]:
            self.assertIn(n, deleted)
        g.add_nonterm(First)
        deleted = g.nonterms_clear()
        self.assertEqual(len(deleted), 1)
        self.assertEqual(deleted, [First])

    def test_clearRules(self):
        g = Grammar(nonterminals=[First, Second, Third],
                    rules=[FirstR, SecondR, ThirdR])
        self.assertEqual(g.rules_count(), 3)
        g.rules_clear()
        self.assertEqual(g.rules_count(), 0)
        g.add_rule(FirstR)
        self.assertEqual(g.rules_count(), 1)
        g.rules_clear()
        self.assertEqual(g.rules_count(), 0)

    def test_clearRulesReturnValue(self):
        g = Grammar(nonterminals=[First, Second, Third],
                    rules=[FirstR, SecondR, ThirdR])
        deleted = g.rules_clear()
        self.assertEqual(len(deleted), 3)
        for r in [FirstR, SecondR, ThirdR]:
            self.assertIn(r, deleted)
        g.add_rule(FirstR)
        deleted = g.rules_clear()
        self.assertEqual(len(deleted), 1)
        self.assertIn(FirstR, deleted)



if __name__ == '__main__':
    main()
