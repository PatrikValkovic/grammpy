#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.12.2024 17:15
:Licence MIT
Part of grammpy

"""
from typing import Any

from .ParsingException import ParsingException


class LLParsingException(ParsingException):
    """
    Exception raised when the LL parsing fails.
    In addition has `position` attribute specifying index of the symbol from input sequence that caused the error.
    """""

    def __init__(self, position, *args):
        # type: (int, Any) -> None
        self.position = position
        super().__init__(*args)

    def __str__(self):
        return f"LL parsing error on symbol at {self.position}: {super().__str__()}"
