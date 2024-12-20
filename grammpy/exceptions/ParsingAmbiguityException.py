#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.12.2024 18:01
:Licence MIT
Part of grammpy

"""
from typing import Any, Type, List, TYPE_CHECKING
from .LLParsingException import LLParsingException

if TYPE_CHECKING:  # pragma: no cover
    from .. import Rule

class ParsingAmbiguityException(LLParsingException):
    """
    There are multiple rules to apply for the current nonterminal and look ahead.
    """

    def __init__(self, position, rules, *args):
        # type: (int, List[Type[Rule]], Any) -> None
        self.rules = rules
        super().__init__(position, *args)

