#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 19.08.2017 17:25
:Licence MIT
Part of grammpy

"""


from unittest import TestCase, main

from grammpy.old_api import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([A], [B, C]),
        ([A], [EPS]),
        ([B], [0, 1])]

class WithEpsilonTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = Grammar()

    def setUp(self):
        self.g = Grammar(terminals=[0, 1],
                         nonterminals=[A, B, C],
                         rules=[Rules])

    def test_removeB(self):
        self.assertEqual(self.g.rules_count(), 3)
        self.g.remove_nonterm(B)
        self.assertEqual(self.g.rules_count(), 1)



if __name__ == '__main__':
    main()