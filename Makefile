DATABASE := serlo.db
DATABASE_TMP := $(shell mktemp -u)
PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)

.PHONY: test $(DATABASE_TMP)

all: $(DATABASE)

$(DATABASE_TMP):
	$(PYTHON) highrise_importer.py 'sqlite:///$@'

$(DATABASE): $(DATABASE_TMP)
	mv '$<' '$@'

test:
	$(PYTHON) -m nose --with-doctest serlo tests
