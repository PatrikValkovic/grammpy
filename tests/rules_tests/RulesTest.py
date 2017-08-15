#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.08.2017 15:31
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import *
from .grammar import *


class RulesTest(TestCase):
    def test_oneRules(self):
        class Tmp1(Rule):
            rules = [([NFirst], [NSecond, 0]),
                     ([NThird], [0, 1]),
                     ([NSecond], [NSecond, 'a'])]
        grammar.add_rule(Tmp1)


if __name__ == '__main__':
    main()
