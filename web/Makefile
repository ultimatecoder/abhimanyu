build:
	yarn install --dev
	pip install pipenv
	pipenv install

build-dev:
	pip install pipenv
	pipenv install --dev

build-static:
	yarn run gulp

unit-test:
	pipenv run pytest

functional-test:
	pipenv run behave

test: unit-test functional-test

run: build-static
	pipenv run flask run
