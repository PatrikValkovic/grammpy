#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.03.2018 16:40
:Licence GPLv3
Part of lambda-cli

"""

class LambdaKeyword:
    pass
class Dot:
    pass
class LeftBracket:
    pass
class RightBracket:
    pass


class Number:
    def __init__(self, value):
        self.value = value
    def __hash__(self):
        return hash(Number)


class Variable:
    def __init__(self, name):
        self.name = name
    def __hash__(self):
        return hash(Variable)


class Parameter:
    def __init__(self, name):
        self.name = name
    def __hash__(self):
        return hash(Parameter)


all_terms = [
    LambdaKeyword,
    Dot,
    Number,
    Variable,
    Parameter,
    LeftBracket,
    RightBracket
]
