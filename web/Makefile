APP := abhimanyu

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
	FLASK_APP=${APP} pipenv run flask run

migrate:
	FLASK_APP=${APP} pipenv run flask db upgrade

create-migrations:
	pipenv run flask db migrate

production-run:
	pipenv run gunicorn -b 127.0.0.1:${port} abhimanyu:app
