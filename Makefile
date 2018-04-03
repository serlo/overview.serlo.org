ROOT_DIR := $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
DATABASE_FILE := $(ROOT_DIR)/serlo.db
DATABASE_TMP_FILE := $(shell mktemp -u)
DATABASE := sqlite:///$(DATABASE_FILE)
DATABASE_TMP := sqlite:///$(DATABASE_TMP_FILE)
PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)

.PHONY: highrise_import, test

highrise_import:
	$(PYTHON) highrise_importer.py '$(DATABASE_TMP)'
	mv '$(DATABASE_TMP_FILE)' '$(DATABASE_FILE)'

test:
	$(PYTHON) -m nose --with-doctest serlo tests
