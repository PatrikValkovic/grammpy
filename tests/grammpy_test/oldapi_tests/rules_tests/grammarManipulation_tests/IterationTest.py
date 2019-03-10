#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 14:08
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import Grammar, Rule as _R
from ..grammar import *


class IterationTest(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.g = Grammar()

    def setUp(self):
        g = Grammar()
        g.add_term([0, 1, 2, 'a', 'b', 'c'])
        g.add_nonterm([NFirst, NSecond, NThird, NFourth])
        self.g = g

    def test_oneRule(self):
        class Tmp(_R):
            rule = ([NFirst], ['a', 0])
        self.g.add_rule(Tmp)
        r = self.g.rules()
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0], Tmp)

    def test_multipleRules(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(_R):
            rule = ([NThird], [0])
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        r = self.g.rules()
        self.assertEqual(len(r), 3)
        for i in [Tmp1, Tmp2, Tmp3]:
            self.assertIn(i, r)


if __name__ == '__main__':
    main()
