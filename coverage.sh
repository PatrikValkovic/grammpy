#!/bin/sh
coverage run --source=pyparsers -m unittest discover -s tests -p "*Test.py"; coverage report -m
