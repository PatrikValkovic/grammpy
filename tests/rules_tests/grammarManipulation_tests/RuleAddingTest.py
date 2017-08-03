#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule, Grammar, Nonterminal as _N


class NFirst(_N):
    pass


class NSecond(_N):
    pass


class NThird(_N):
    pass


class NFourth(_N):
    pass


class RuleAddingTest(TestCase):
    def __init__(self):
        super().__init__()
        self.g = None

    def setUp(self):
        g = Grammar()
        g.add_term([0, 1, 2, 'a', 'b', 'c'])
        g.add_nonterm([NFirst, NSecond, NThird, NFourth])


if __name__ == '__main__':
    main()
