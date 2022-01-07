PYTHON = python3

help:
	@echo "install:          Initialize the environment"
	@echo "test:             To test the project"
	@echo "run:              To run the project"
	@echo "shell:            To run pshell locally"
	@echo "celery:           To run celery"
	@echo "redis:            To up broker"


install:
	pip install setuptools==59.6.0
	pip install -e .
	pip install poetry
	poetry install

test:
	poetry run pytest -vv

run:
	pserve development.ini

shell:
	pshell development.ini

celery:
	celery --app=pyramid_celery.celery_app worker --ini development.ini -l INFO

redis:
	docker run -d -p 6379:6379 redis
