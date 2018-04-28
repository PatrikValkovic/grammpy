#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 11:10
:Licence GNUv3
Part of grammpy

"""

from .GrammpyException import GrammpyException


class TreeDeletedException(GrammpyException):
    """
    Exception that parent of the AST was already deleted
    """
    pass
