#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 28.07.2017 09:12
:Licence MIT
Part of grammpy

"""
from typing import Any

from .GrammpyException import GrammpyException


class NotNonterminalException(GrammpyException, TypeError):
    """
    Object is not Nonterminal class
    """
    def __init__(self, parameter, *args: Any) -> None:
        super().__init__(*args)
        self.object = parameter
