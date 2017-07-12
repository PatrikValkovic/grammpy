#!/bin/sh
coverage run --source=grammpy -m unittest discover -s tests -p "*Test.py"; coverage report -m
