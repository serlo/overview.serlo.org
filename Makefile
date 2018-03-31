PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)

.PHONY: highrise_import, test

highrise_import:
	$(PYTHON) highrise_importer.py

test:
	$(PYTHON) -m nose --with-doctest serlo
