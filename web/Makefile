build: migrate
	yarn install --dev
	pip install pipenv
	pipenv install

build-dev: migrate
	yarn install --dev
	pip install pipenv
	pipenv install --dev

build-static:
	yarn run gulp

unit-test:
	PYTHONPATH=${PWD} pipenv run pytest

functional-test:
	PYTHONPATH=${PWD} SQLALCHEMY_DATABASE_URI='sqlite:///${PWD}/temp.db' pipenv run behave

test: unit-test functional-test

run: build-static
	pipenv run flask run

migrate:
	pipenv run flask db upgrade

create-migrations:
	pipenv run flask db migrate
