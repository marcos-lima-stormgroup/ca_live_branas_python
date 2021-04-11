DEVPI_URL ?= https://devpi.qa.stormsec.com.br/deploy/dev
CI_ENVIRONMENT_NAME ?= dev
APIDOC_TITLE = "LegalPharma Backend API"
APIDOC_DESCRIPTION = "Documentação da API do sistema LegalPharma"
APIDOC_VERSION = "0.1.0"

.PHONY: clean clean-test clean-pyc clean-build docs help tests uninstall_all
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

define UNINSTALL_ALL_PYSCRIPT
import os
req = 'requirements.txt'
for package in [x.split('==')[0] for x in open(req).read().split('\n')]:
	if package.strip():
		os.system('pip uninstall --yes %s' % package)

endef
export UNINSTALL_ALL_PYSCRIPT

uninstall_all:
	@python -c "$$UNINSTALL_ALL_PYSCRIPT"

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

tests:
	python3 -m pytest -s -vv -m "not slow" --cov=tests --cov=parking_lot -W ignore::DeprecationWarning --cov-report term-missing:skip-covered --ignore=pg_data
	@echo "Linting..."
	@flake8 parking_lot/ --max-complexity=5 --exclude parking_lot/infra/repository/parking_lot_sql_queries.py
	@flake8 tests/ --ignore=S101,S311,F811,S605,S607
	@echo "\033[32mTudo certo!"

install_dev: clean install ## instala as dependências de desenvolvimento
	pip install -r requirements_dev.txt

install: clean uninstall_all ## instala as dependências do projeto
	pip install devpi-client
	devpi use $(DEVPI_URL) --always-set-cfg=yes
	pip install -r requirements.txt

deploy: clean install ## Executa o chalice deploy.
	chalice deploy --stage $(CI_ENVIRONMENT_NAME) | tee deploy.log

apidoc:
	chalice_support apidoc --output doc --title $(APIDOC_TITLE) --description $(APIDOC_DESCRIPTION) --version $(APIDOC_VERSION)
