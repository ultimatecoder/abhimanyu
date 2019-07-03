build:
	yarn install --dev
build-static:
	yarn run gulp
unit-test:
	pipenv run pytest
test: unit-test
run: build-static
	pipenv run flask run
