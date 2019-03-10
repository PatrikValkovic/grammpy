#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import Rule as _R, Grammar
from ..grammar import *


class ValidAddTest(TestCase):
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

        self.assertEqual(self.g.rules_count(), 0)
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertIsNone(self.g.get_rule(Tmp))
        self.assertIsNone(self.g.rule(Tmp))
        self.assertEqual(self.g.add_rule(Tmp)[0].rule, Tmp.rule)
        self.assertEqual(self.g.rules_count(), 1)
        self.assertTrue(self.g.have_rule(Tmp))
        self.assertEqual(self.g.get_rule(Tmp), Tmp)
        self.assertEqual(self.g.rule(Tmp), Tmp)

    def test_addOneInArray(self):
        class Tmp(_R):
            rule = ([NFirst], ['a', 0])

        self.assertEqual(self.g.rules_count(), 0)
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertIsNone(self.g.get_rule(Tmp))
        self.assertIsNone(self.g.rule(Tmp))
        self.assertEqual(self.g.add_rule([Tmp])[0].rule, ([NFirst], ['a', 0]))
        self.assertEqual(self.g.rules_count(), 1)
        self.assertTrue(self.g.have_rule(Tmp))
        self.assertEqual(self.g.get_rule(Tmp), Tmp)
        self.assertEqual(self.g.rule(Tmp), Tmp)

    def test_addOneInTuple(self):
        class Tmp(_R):
            rule = ([NFirst], ['a', 0])

        self.assertEqual(self.g.rules_count(), 0)
        self.assertFalse(self.g.have_rule(Tmp))
        self.assertIsNone(self.g.get_rule(Tmp))
        self.assertIsNone(self.g.rule(Tmp))
        self.assertEqual(self.g.add_rule((Tmp,))[0].rule, Tmp.rule)
        self.assertEqual(self.g.rules_count(), 1)
        self.assertTrue(self.g.have_rule(Tmp))
        self.assertEqual(self.g.get_rule(Tmp), Tmp)
        self.assertEqual(self.g.rule(Tmp), Tmp)

    def test_addThree(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])

        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])

        class Tmp3(_R):
            rule = ([NThird], [0])

        self.assertEqual(self.g.rules_count(), 0)
        self.assertFalse(self.g.have_rule(Tmp1))
        self.assertIsNone(self.g.get_rule(Tmp1))
        self.assertIsNone(self.g.rule(Tmp1))
        self.assertFalse(self.g.have_rule(Tmp2))
        self.assertIsNone(self.g.get_rule(Tmp2))
        self.assertIsNone(self.g.rule(Tmp2))
        self.assertFalse(self.g.have_rule(Tmp3))
        self.assertIsNone(self.g.get_rule(Tmp3))
        self.assertIsNone(self.g.rule(Tmp3))
        self.assertEqual(self.g.add_rule(Tmp1)[0].rule, Tmp1.rule)
        self.assertEqual(self.g.rules_count(), 1)
        self.assertTrue(self.g.have_rule(Tmp1))
        self.assertEqual(self.g.get_rule(Tmp1), Tmp1)
        self.assertEqual(self.g.rule(Tmp1), Tmp1)
        self.assertFalse(self.g.have_rule(Tmp2))
        self.assertIsNone(self.g.get_rule(Tmp2))
        self.assertIsNone(self.g.rule(Tmp2))
        self.assertFalse(self.g.have_rule(Tmp3))
        self.assertIsNone(self.g.get_rule(Tmp3))
        self.assertIsNone(self.g.rule(Tmp3))
        self.assertEqual(self.g.add_rule(Tmp2)[0].rule, Tmp2.rule)
        self.assertEqual(self.g.rules_count(), 2)
        self.assertTrue(self.g.have_rule(Tmp1))
        self.assertEqual(self.g.get_rule(Tmp1), Tmp1)
        self.assertEqual(self.g.rule(Tmp1), Tmp1)
        self.assertTrue(self.g.have_rule(Tmp2))
        self.assertEqual(self.g.get_rule(Tmp2), Tmp2)
        self.assertEqual(self.g.rule(Tmp2), Tmp2)
        self.assertFalse(self.g.have_rule(Tmp3))
        self.assertIsNone(self.g.get_rule(Tmp3))
        self.assertIsNone(self.g.rule(Tmp3))
        self.assertEqual(self.g.add_rule(Tmp3)[0].rule, Tmp3.rule)
        self.assertEqual(self.g.rules_count(), 3)
        self.assertTrue(self.g.have_rule(Tmp1))
        self.assertEqual(self.g.get_rule(Tmp1), Tmp1)
        self.assertEqual(self.g.rule(Tmp1), Tmp1)
        self.assertTrue(self.g.have_rule(Tmp2))
        self.assertEqual(self.g.get_rule(Tmp2), Tmp2)
        self.assertEqual(self.g.rule(Tmp2), Tmp2)
        self.assertTrue(self.g.have_rule(Tmp3))
        self.assertEqual(self.g.get_rule(Tmp3), Tmp3)
        self.assertEqual(self.g.rule(Tmp3), Tmp3)

    def test_addThreeInArray(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])

        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])

        class Tmp3(_R):
            rule = ([NThird], [0])

        self.assertEqual(self.g.rules_count(), 0)
        add = self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.assertEqual(add[0].rule, Tmp1.rule)
        self.assertEqual(add[1].rule, Tmp2.rule)
        self.assertEqual(add[2].rule, Tmp3.rule)
        self.assertEqual(self.g.rules_count(), 3)
        self.assertTrue(self.g.have_rule(Tmp1))
        self.assertEqual(self.g.get_rule(Tmp1), Tmp1)
        self.assertEqual(self.g.rule(Tmp1), Tmp1)
        self.assertTrue(self.g.have_rule(Tmp2))
        self.assertEqual(self.g.get_rule(Tmp2), Tmp2)
        self.assertEqual(self.g.rule(Tmp2), Tmp2)
        self.assertTrue(self.g.have_rule(Tmp3))
        self.assertEqual(self.g.get_rule(Tmp3), Tmp3)
        self.assertEqual(self.g.rule(Tmp3), Tmp3)

    def test_addThreeInTuple(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])

        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])

        class Tmp3(_R):
            rule = ([NThird], [0])

        self.assertEqual(self.g.rules_count(), 0)
        add = self.g.add_rule((Tmp1, Tmp2, Tmp3))
        self.assertEqual(add[0].rule, Tmp1.rule)
        self.assertEqual(add[1].rule, Tmp2.rule)
        self.assertEqual(add[2].rule, Tmp3.rule)
        self.assertEqual(self.g.rules_count(), 3)
        self.assertTrue(self.g.have_rule(Tmp1))
        self.assertEqual(self.g.get_rule(Tmp1), Tmp1)
        self.assertEqual(self.g.rule(Tmp1), Tmp1)
        self.assertTrue(self.g.have_rule(Tmp2))
        self.assertEqual(self.g.get_rule(Tmp2), Tmp2)
        self.assertEqual(self.g.rule(Tmp2), Tmp2)
        self.assertTrue(self.g.have_rule(Tmp3))
        self.assertEqual(self.g.get_rule(Tmp3), Tmp3)
        self.assertEqual(self.g.rule(Tmp3), Tmp3)

    def test_shouldAddIntoGrammar(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])

        g = Grammar(terminals=['a', 0],
                    nonterminals=[NFirst],
                    rules=[Tmp1])
        g.add_rule(Tmp1)
        self.assertEqual(g.get_rule(Tmp1), Tmp1)


if __name__ == '__main__':
    main()
