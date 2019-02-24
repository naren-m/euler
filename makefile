.PHONY: help test format clean

.DEFAULT: help
help:
	@echo "make test       run tests"
	@echo "make coverage   generate code coverage report"
	@echo "make clean      clean workspace"
	@echo "make format     run yapf formatter"

test: clean
	(cd euler; python3 -m unittest)

clean: clean-pyc clean-coverage
		find . -name '*.swp' -exec rm -rf {} +
		find . -name '*.bak' -exec rm -rf {} +

clean-coverage:
	rm -rf htmlcov

clean-pyc: ## remove Python file artifacts
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		find . -name '__pycache__' -exec rm -rf {} +


format: clean
	yapf -r -i .