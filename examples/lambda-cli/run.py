#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.04.2018 19:08
:Licence GPLv3
Part of lambda-cli

"""

from lambda_cli import steps
from lambda_cli.exceptions import ParsingException, LexException


def run():
    while True:
        i = input('>>>')
        if i == 'exit':
            break
        try:
            for r in steps(i):
                print(r)
        except (LexException, ParsingException):
            print('Invalid input')


if __name__ == '__main__':
    run()