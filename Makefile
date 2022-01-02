PYTHON = python3

.PHONY = help setup test run clean

FILES = input output

.DEFAULT_GOAL = help


help:
	@echo -e "install:			Initialize the environment"
	@echo -e "test:				To test the project
	@echo -e "run:				To run the project"


install:
	pip install setuptools==59.6.0
	pip install poetry
	poetry install -vvv

test:
	pytest -vv

run:
	pserve development.ini