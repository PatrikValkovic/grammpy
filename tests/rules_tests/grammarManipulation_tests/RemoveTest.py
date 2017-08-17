#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 14:44
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase

from grammpy import Rule as _R, Grammar
from ..grammar import *


class RemoveTest(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.g = Grammar()

    def setUp(self):
        g = Grammar()
        g.add_term([0, 1, 2, 'a', 'b', 'c'])
        g.add_nonterm([NFirst, NSecond, NThird, NFourth])
        self.g = g

    def test_removeOneFromOne(self):
        class Tmp(_R):
            rule = ([NFirst], ['a', 0])
        self.g.add_rule(Tmp)
        self.assertEqual(self.g.rules_count(), 1)
        self.assertTrue(self.g.have_rule(Tmp))
        self.assertEqual(self.g.remove_rule(Tmp)[0].rule, Tmp.rule)
        self.assertEqual(self.g.rules_count(), 0)
        self.assertFalse(self.g.have_rule(Tmp))

    def test_removeOneFromMore(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(_R):
            rule = ([NThird], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.assertEqual(self.g.rules_count(), 3)
        self.assertTrue(self.g.have_rule([Tmp1, Tmp2, Tmp3]))
        self.assertEqual(self.g.remove_rule(Tmp2)[0].rule, Tmp2.rule)
        self.assertEqual(self.g.rules_count(), 2)
        self.assertTrue(self.g.have_rule([Tmp1, Tmp3]))

    def test_removeTwoFromTwo(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        self.g.add_rule([Tmp1, Tmp2])
        self.assertEqual(self.g.rules_count(), 2)
        self.assertTrue(self.g.have_rule([Tmp1, Tmp2]))
        delete = self.g.remove_rule([Tmp1, Tmp2])
        self.assertEqual(delete[0].rule, Tmp1.rule)
        self.assertEqual(delete[1].rule, Tmp2.rule)
        self.assertEqual(self.g.rules_count(), 0)
        self.assertFalse(self.g.have_rule([Tmp1]))
        self.assertFalse(self.g.have_rule([Tmp2]))

    def test_removeTwoFromMore(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(_R):
            rule = ([NThird], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.assertEqual(self.g.rules_count(), 3)
        self.assertTrue(self.g.have_rule([Tmp1, Tmp2, Tmp3]))
        delete = self.g.remove_rule([Tmp1, Tmp2])
        self.assertEqual(delete[0].rule, Tmp1.rule)
        self.assertEqual(delete[1].rule, Tmp2.rule)
        self.assertEqual(self.g.rules_count(), 1)
        self.assertTrue(self.g.have_rule(Tmp3))
        self.assertFalse(self.g.have_rule([Tmp1]))
        self.assertFalse(self.g.have_rule([Tmp2]))

    def test_removeAll(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(_R):
            rule = ([NThird], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.assertEqual(self.g.rules_count(), 3)
        self.assertTrue(self.g.have_rule([Tmp1, Tmp2, Tmp3]))
        delete = self.g.remove_rule()
        for r in [Tmp1, Tmp2, Tmp3]:
            self.assertIn(r, delete)
        self.assertEqual(self.g.rules_count(), 0)
        self.assertFalse(self.g.have_rule([Tmp1]))
        self.assertFalse(self.g.have_rule([Tmp2]))
        self.assertFalse(self.g.have_rule([Tmp3]))


if __name__ == '__main__':
    main()
