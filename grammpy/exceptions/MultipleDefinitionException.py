#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:25
:Licence MIT
Part of grammpy

"""

from .RuleSyntaxException import RuleSyntaxException


class MultipleDefinitionException(RuleSyntaxException):
    """
    The rule is defined multiple times.
    """

    def __init__(self, rule, message, additional=None):
        super().__init__(rule, message, additional)
