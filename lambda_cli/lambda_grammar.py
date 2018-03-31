#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 15:45
:Licence GNUv3
Part of lambda-cli

"""

from grammpy import Grammar, Nonterminal, Rule
import interpreter
from .terminals import *

class Expression(Nonterminal):
    def get_representation(self):
        return self.to_rule.to_symbols[1].get_representation()
class Lambda(Nonterminal):
    def get_representation(self):
        parameters = list(self.to_rule.to_symbols[2].parameters())
        expression = self.to_rule.to_symbols[-2].get_representation()
        return interpreter.Lambda(parameters, expression)
class Parameters(Nonterminal):
    def parameters(self):
        term = self.to_rule.to_symbols[0].s #type: Parameter
        yield term.name
        try:
            yield from self.to_rule.to_symbols[1].parameters
        except IndexError:
            return
class NoBracketExpression(Nonterminal):
    def get_representation(self):
        body = list(self.to_rule.to_symbols[0].get_body())
        return interpreter.Expression(body)
class ExpressionBody(Nonterminal):
    def get_body(self):
        return self.to_rule.get_body()


class ExpressionBodyToVariable(Rule):
    rules = [
        ([ExpressionBody], [Variable, ExpressionBody]),
        ([ExpressionBody], [Variable])
    ]
    def get_body(self):
        variable = self.to_symbols[0].s #type: Variable
        yield interpreter.Variable(variable.name)
        try:
            yield from self.to_symbols[1].get_body()
        except IndexError:
            return


class ExpressionBodyToNumber(Rule):
    rules = [
        ([ExpressionBody], [Number, ExpressionBody]),
        ([ExpressionBody], [Number])
    ]
    def get_body(self):
        num = self.to_symbols[0].s #type: Number
        yield interpreter.Variable(num.value)
        try:
            yield from self.to_symbols[1].get_body()
        except IndexError:
            return


class ExpressionBodyToLambda(Rule):
    rules = [
        ([ExpressionBody], [Lambda, ExpressionBody]),
        ([ExpressionBody], [Lambda])
    ]
    def get_body(self):
        l = self.to_symbols[0].s #type: Lambda
        yield l.get_representation()
        try:
            yield from self.to_symbols[1].get_body()
        except IndexError:
            return


class ExpressionBodyToExpression(Rule):
    rules = [
        ([ExpressionBody], [Expression, ExpressionBody]),
        ([ExpressionBody], [Expression])
    ]
    def get_body(self):
        expr = self.to_symbols[0] #type: Expression
        yield expr.get_representation()
        try:
            yield from self.to_symbols[1].get_body()
        except IndexError:
            return


class NoBracketExpressionRule(Rule):
    fromSymbol = NoBracketExpression
    toSymbol = ExpressionBody


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
        ExpressionBody,
        Lambda,
        Parameters
    ],
    rules=[
        NoBracketExpressionRule,
        ExpressionBodyToExpression,
        ExpressionBodyToLambda,
        ExpressionBodyToNumber,
        ExpressionBodyToVariable,
        ExpressionRule,
        LambdaRule,
        ParametersRule
    ],
    start_symbol=NoBracketExpression)
