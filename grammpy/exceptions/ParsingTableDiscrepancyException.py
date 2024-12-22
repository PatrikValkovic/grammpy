#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.12.2024 17:36
:Licence MIT
Part of grammpy

"""
from .LLParsingException import LLParsingException

class ParsingTableDiscrepancyException(LLParsingException):
    """
    Exception raised when the nonterminal on the stack doesn't match the nonterminal in the input sequence.
    This should never happen and in general points to discrepancy between the parsing table and the rule.
    The rule probably doesn't generate the terminal that is in the look-ahead sequence.
    """
    pass
