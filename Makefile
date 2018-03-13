PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)

.PHONY: test

test:
	$(PYTHON) -m nose --with-doctest serlo
