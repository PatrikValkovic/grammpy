#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 15:44
:Licence GNUv3
Part of lambda-cli

"""



from unittest import TestCase, main
from pyparsers import cyk
from lambda_cli import lambda_grammar


class ParsingTest(TestCase):
    def test_alpha_reduction(self):
        cyk(lambda_grammar, "((lambda x y. (x y)) y)")
        cyk(lambda_grammar, "(lambda y'. (y y'))")
        cyk(lambda_grammar, "((lambda x. (lambda z. (x z))) (z g))")
        cyk(lambda_grammar, "(lambda z'. ((z g) z'))")
        cyk(lambda_grammar, "((lambda y. (lambda z. (z y))) y z)")
        cyk(lambda_grammar, "(z y)")
        cyk(lambda_grammar, "((lambda x. (lambda y. (y (lambda x. x) x))) x)")
        cyk(lambda_grammar, "(lambda y. (y (lambda x'. x') x))")

    def test_applicative(self):
        cyk(lambda_grammar, "((lambda x. x) (lambda y. y) (lambda z. z))")
        cyk(lambda_grammar, "((lambda y. y) (lambda z. z))")
        cyk(lambda_grammar, "(lambda x. ((lambda y. y) 2 x))")
        cyk(lambda_grammar, "(x y (lambda x. ((lambda y. x) 3)))")
        cyk(lambda_grammar, "((lambda x y. ((lambda z. ((lambda f. (z f)) z)) x)) 3 7)")

    def test_expression(self):
        cyk(lambda_grammar, "(a (lambda b. (x (lambda c. (y t (lambda y x c. 12))))) 13 p (lambda x. (2 3)))")
        cyk(lambda_grammar, "(x y z a b)")
        cyk(lambda_grammar, "((lambda x. ((lambda y. (y x)) x y)) z)")
        cyk(lambda_grammar, "((lambda x. (x y)) 8)")

    def test_longer_variables(self):
        cyk(lambda_grammar, "((lambda x y. (x y)) y)")
        cyk(lambda_grammar, "((lambda hello. (x y)) y)")
        cyk(lambda_grammar, "((lambda here y. ((lambda z. ((lambda f. (z f)) z)) here)) 3 7)")




if __name__ == '__main__':
    main()
