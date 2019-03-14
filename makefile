.PHONY: help test format clean

.DEFAULT: help
help:
	@echo "make test       run tests"
	@echo "make coverage   generate code coverage report"
	@echo "make clean      clean workspace"
	@echo "make format     run yapf formatter"

test: clean
	(cd euler; python3 -m unittest discover)

clean: clean-pyc clean-coverage clean-dist
		find . -name '*.swp' -exec rm -rf {} +
		find . -name '*.bak' -exec rm -rf {} +

clean-dist:
		find . -name '*.egg-info' -exec rm -rf {} +
		rm -rf dist
		rm -rf build

clean-coverage:
	rm -rf htmlcov

clean-pyc: ## remove Python file artifacts
		find . -name '*.pyc' -exec rm -f {} +
		find . -name '*.pyo' -exec rm -f {} +
		find . -name '*~' -exec rm -f {} +
		find . -name '__pycache__' -exec rm -rf {} +
		find . -name '.eggs' -exec rm -rf {} +

format: clean
	yapf -r -i .

install: clean
	pip3 install -e .

build:
	python3 setup.py bdist_wheel

release: clean clean-dist build
	twine upload dist/*

coverage: clean
	coverage run --source euler setup.py test
	coverage html
