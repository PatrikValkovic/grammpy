.phony: test

test:
	python -W ignore::DeprecationWarning -m unittest discover -s tests -p "*Test.py"

coverage:
	coverage run --source=grammpy -m unittest discover -s tests -p "*Test.py"
	coverage report -m