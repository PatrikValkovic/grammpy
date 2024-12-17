#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.03.2019 18:14
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.parsers import cyk
from grammpy.transforms import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass



class OrderedTraversingTest(TestCase):
    def test_nonterminalToTerm(self):
        class Rule1(Rule): rule=([A], [0])
        g = Grammar(terminals=[0],
                    nonterminals=[A],
                    rules=[Rule1],
                    start_symbol=A)
        root = cyk(g, [0])
        representaton = Traversing.print(root)
        expect = \
"""
(N)A
`--(R)Rule1
   `--(T)0
""".lstrip()
        self.assertEqual(representaton, expect)

    def test_splitTest(self):
        class Rule1(Rule): rule=([A], [B, C])
        class Rule2(Rule): rule=([B], [0])
        class Rule3(Rule): rule=([C], [1])
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C],
                    rules=[Rule1, Rule2, Rule3],
                    start_symbol=A)
        root = cyk(g, [0, 1])
        representation = Traversing.print(root)
        expect = \
"""
(N)A
`--(R)Rule1
   |--(N)B
   |  `--(R)Rule2
   |     `--(T)0
   `--(N)C
      `--(R)Rule3
         `--(T)1
""".lstrip()
        self.assertEqual(representation, expect)

    def test_recursiveTest(self):
        class Rule0(Rule): rule=([A], [A, 2])
        class Rule1(Rule): rule=([A], [B, C])
        class Rule2(Rule): rule=([B], [0])
        class Rule3(Rule): rule=([C], [1])
        g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[A, B, C],
                    rules=[Rule0, Rule1, Rule2, Rule3],
                    start_symbol=A)
        ContextFree.prepare_for_cyk(g, True)
        root = cyk(g, [0, 1, 2, 2])
        root = InverseContextFree.reverse_cyk_transforms(root)
        representation = Traversing.print(root)
        expect = \
"""
(N)A
`--(R)Rule0
   |--(N)A
   |  `--(R)Rule0
   |     |--(N)A
   |     |  `--(R)Rule1
   |     |     |--(N)B
   |     |     |  `--(R)Rule2
   |     |     |     `--(T)0
   |     |     `--(N)C
   |     |        `--(R)Rule3
   |     |           `--(T)1
   |     `--(T)2
   `--(T)2
""".lstrip()
        self.assertEqual(representation, expect)


if __name__ == '__main__':
    main()
