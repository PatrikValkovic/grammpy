#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 12.03.2019 13:37
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *

class N1(Nonterminal): pass
class N2(Nonterminal): pass
class N3(Nonterminal): pass
class R1(Rule): rule=([N1], [0])
class R2(Rule): rule=([N2], [N1, 0])
class R3(Rule): rule=([N3], [1, 2, 1])


class WithNonterminalTest(TestCase):
    def test_removeInOne(self):
        g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[N1, N2, N3],
                    rules=[R1, R2, R3])
        class Tmp(Rule):
            rule = ([N3], [1, 2, 1])
        g.nonterminals.remove(N3)
        self.assertEqual(g.rules.size(), 2)
        self.assertNotIn(Tmp, g.rules)
        self.assertIn(R1, g.rules)
        self.assertIn(R2, g.rules)
        self.assertNotIn(R3, g.rules)

    def test_removeTwoRules(self):
        g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[N1, N2, N3],
                    rules=[R1, R2, R3])
        class Tmp1(Rule):
            rule = ([N1], [0])
        class Tmp2(Rule):
            rule = ([N2], [N1, 0])
        g.nonterminals.remove(N1)
        self.assertEqual(g.rules.size(), 1)
        self.assertNotIn(Tmp1, g.rules)
        self.assertNotIn(Tmp2, g.rules)
        self.assertNotIn(R1, g.rules)
        self.assertNotIn(R2, g.rules)
        self.assertIn(R3, g.rules)

    def test_removeAll(self):
        g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[N1, N2, N3],
                    rules=[R1, R2, R3])
        g.nonterminals.remove(N1, N3)
        self.assertEqual(g.rules.size(), 0)
        self.assertNotIn(R1, g.rules)
        self.assertNotIn(R2, g.rules)
        self.assertNotIn(R3, g.rules)


if __name__ == '__main__':
    main()
