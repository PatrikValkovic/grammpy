#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 28.04.2018 19:06
:Licence MIT
Part of grammpy

"""

from .GrammpyException import GrammpyException


class StartSymbolNotSetException(GrammpyException, ValueError):
    """
    Represent error when the start symbol of the grammar is not set and is required.
    """
    pass
