PYTHON := python
UV := uv

.PHONY: help sync install sync-types sync-types-update generate lint typecheck test check build release-dry

help:
	@echo "Available targets:"
	@echo "  make install           - install all dependencies with uv"
	@echo "  make sync              - alias for install"
	@echo "  make sync-types        - generate Python ServiceStack references with x tool"
	@echo "  make sync-types-update - update existing *.dtos.py references with x tool"
	@echo "  make generate          - regenerate SDK modules/tests/docs"
	@echo "  make lint              - run ruff"
	@echo "  make typecheck         - run mypy"
	@echo "  make test              - run pytest"
	@echo "  make check             - run lint + typecheck + tests"
	@echo "  make build             - build wheel/sdist"
	@echo "  make release-dry       - semantic-release dry run (no publish)"

install:
	$(UV) sync --all-groups

sync: install

sync-types:
	$(UV) run $(PYTHON) scripts/sync_types.py

sync-types-update:
	$(UV) run $(PYTHON) scripts/sync_types.py --update-only

generate:
	$(UV) run $(PYTHON) scripts/generate_endpoints.py

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
