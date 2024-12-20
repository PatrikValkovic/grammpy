#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.12.2024 17:56
:Licence MIT
Part of grammpy

"""
from .LLParsingException import LLParsingException

class NoRuleForLookAheadException(LLParsingException):
    """
    There is no rule to apply for the current nonterminal and look ahead.
    """
    pass