#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule as _R, Grammar, Nonterminal as _N


class NFirst(_N):
    pass


class NSecond(_N):
    pass


class NThird(_N):
    pass


class NFourth(_N):
    pass


class RuleAddingTest(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.g = Grammar()

    def setUp(self):
        g = Grammar()
        g.add_term([0, 1, 2, 'a', 'b', 'c'])
        g.add_nonterm([NFirst, NSecond, NThird, NFourth])
        self.g = g

    def test_addOne(self):
        class Tmp(_R):
            rule = ([NFirst], ['a', 0])
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertIsNone(self.g.get_rule(Tmp))
        self.assertIsNone(self.g.rule(Tmp))
        self.g.add_rule(Tmp)
        self.assertTrue(self.g.have_rule(Tmp))
        self.assertEqual(self.g.get_rule(Tmp), Tmp)
        self.assertEqual(self.g.rule(Tmp), Tmp)

    def test_addOneInArray(self):
        class Tmp(_R):
            rule = ([NFirst], ['a', 0])
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertIsNone(self.g.get_rule(Tmp))
        self.assertIsNone(self.g.rule(Tmp))
        self.g.add_rule([Tmp])
        self.assertTrue(self.g.have_rule(Tmp))
        self.assertEqual(self.g.get_rule(Tmp), Tmp)
        self.assertEqual(self.g.rule(Tmp), Tmp)

    def test_addOneInTuple(self):
        class Tmp(_R):
            rule = ([NFirst], ['a', 0])
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertIsNone(self.g.get_rule(Tmp))
        self.assertIsNone(self.g.rule(Tmp))
        self.g.add_rule((Tmp,))
        self.assertTrue(self.g.have_rule(Tmp))
        self.assertEqual(self.g.get_rule(Tmp), Tmp)
        self.assertEqual(self.g.rule(Tmp), Tmp)


if __name__ == '__main__':
    main()
