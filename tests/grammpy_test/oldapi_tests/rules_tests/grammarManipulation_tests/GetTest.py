#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 14:41
:Licence MIT
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import Rule as _R, Grammar
from ..grammar import *


class GetTest(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.g = Grammar()

    def setUp(self):
        g = Grammar()
        g.add_term([0, 1, 2, 'a', 'b', 'c'])
        g.add_nonterm([NFirst, NSecond, NThird, NFourth])
        self.g = g

    def test_getAsArray(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(_R):
            rule = ([NThird], [0])
        self.assertEqual(self.g.rules_count(), 0)
        self.g.add_rule([Tmp1, Tmp2, Tmp3])
        self.assertEqual(self.g.get_rule([Tmp1, Tmp2, Tmp3]), [Tmp1, Tmp2, Tmp3])

    def test_getOne(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        self.assertEqual(self.g.rules_count(), 0)
        self.g.add_rule([Tmp1])
        self.assertEqual(self.g.get_rule(Tmp1), Tmp1)


    def test_getAsArrayWithNone(self):
        class Tmp1(_R):
            rule = ([NFirst], ['a', 0])
        class Tmp2(_R):
            rule = ([NSecond], ['a', 0, NFourth])
        class Tmp3(_R):
            rule = ([NThird], [0])
        self.assertEqual(self.g.rules_count(), 0)
        self.g.add_rule([Tmp1, Tmp3])
        self.assertEqual(self.g.get_rule([Tmp1, Tmp2, Tmp3]), [Tmp1, None, Tmp3])


if __name__ == '__main__':
    main()
