#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 27.04.2018 17:49
:Licence GPLv3
Part of grammpy

"""

from .ParsingException import ParsingException

class NotParsedException(ParsingException):
    """
    Represent exception that the tree was not parsed successfully
    """
    pass
