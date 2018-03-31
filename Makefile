ROOT_DIR := $(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))
DATABASE := sqlite:///$(ROOT_DIR)/serlo.db
PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)

.PHONY: highrise_import, test

highrise_import:
	$(PYTHON) highrise_importer.py '$(DATABASE)'

test:
	$(PYTHON) -m nose --with-doctest serlo
