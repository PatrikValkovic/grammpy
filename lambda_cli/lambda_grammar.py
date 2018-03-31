#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 15:45
:Licence GNUv3
Part of lambda-cli

"""

from grammpy import Grammar, Nonterminal, Rule
from .terminals import *


class Expression(Nonterminal):
    pass
class Lambda(Nonterminal):
    pass
class Parameters(Nonterminal):
    pass
class NoBracketExpression(Nonterminal):
    pass


class NoBracketExpressionRule(Rule):
    rules = [
        ([NoBracketExpression], [Variable, NoBracketExpression]),
        ([NoBracketExpression], [Number, NoBracketExpression]),
        ([NoBracketExpression], [Lambda, NoBracketExpression]),
        ([NoBracketExpression], [Expression, NoBracketExpression]),
        ([NoBracketExpression], [Variable]),
        ([NoBracketExpression], [Number]),
        ([NoBracketExpression], [Lambda]),
        ([NoBracketExpression], [Expression])
    ]


class ExpressionRule(Rule):
    fromSymbol = Expression
    right = [LeftBracket, NoBracketExpression, RightBracket]


class LambdaRule(Rule):
    fromSymbol = Lambda
    right = [LeftBracket, LambdaKeyword, Parameters, Dot, NoBracketExpression, RightBracket]


class ParametersRule(Rule):
    rules = [
        ([Parameters], [Parameter, Parameters]),
        ([Parameters], [Parameter])
    ]

lambda_grammar = Grammar(
    terminals=all_terms,
    nonterminals=[
        NoBracketExpression,
        Expression,
        Lambda,
        Parameters
    ],
    rules=[
        NoBracketExpressionRule,
        ExpressionRule,
        LambdaRule,
        ParametersRule
    ],
    start_symbol=NoBracketExpression)
