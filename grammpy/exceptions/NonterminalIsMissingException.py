#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.12.2024 17:43
:Licence MIT
Part of grammpy

"""
from typing import Any, TYPE_CHECKING, Type
from .LLParsingException import LLParsingException

if TYPE_CHECKING:  # pragma: no cover
    from .. import Nonterminal

class NonterminalIsMissingException(LLParsingException):
    """
    Exception that occurs when there is nonterminal on top of the stack that has no entry in the parsing table.
    This should not happen in general and suggest there are some problems with the grammar.
    """

    def __init__(self, position, nonterminal, *args):
        # type: (int, Type[Nonterminal], Any) -> None
        self.nonterminal = nonterminal
        super().__init__(position, *args)
