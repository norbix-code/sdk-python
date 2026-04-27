PYTHON := python
UV := uv

.PHONY: help sync install lint typecheck test check build release-dry

help:
	@echo "Available targets:"
	@echo "  make install           - install all dependencies with uv"
	@echo "  make sync              - alias for install"
	@echo "  make lint              - run ruff"
	@echo "  make typecheck         - run mypy"
	@echo "  make test              - run pytest"
	@echo "  make check             - run lint + typecheck + tests"
	@echo "  make build             - build wheel/sdist"
	@echo "  make release-dry       - semantic-release dry run (no publish)"

install:
	$(UV) sync --all-groups

sync: install

lint:
	$(UV) run ruff check .

typecheck:
	$(UV) run mypy src

test:
	$(UV) run pytest

check: lint typecheck test

build:
	$(UV) build

release-dry:
	$(UV) run semantic-release --noop version
