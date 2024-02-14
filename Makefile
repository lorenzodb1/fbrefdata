.PHONY: init test lint pretty

BIN = .venv/bin/
CODE = fbrefdata
PY = 3.11

init:
	python3 -m venv .venv
	poetry install

test:
	nox -rs tests-$(PY) -- $(args)

mypy:
	nox -rs mypy-$(PY) -- $(args)

lint:
	nox -rs pre-commit -- $(args)

precommit_install:
	nox -rs pre-commit -- install

bump_major:
	$(BIN)bumpversion major

bump_minor:
	$(BIN)bumpversion minor

bump_patch:
	$(BIN)bumpversion patch

clean:
	rm -rf .venv
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
