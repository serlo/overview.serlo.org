PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)
TEMPLATE := report.html

DATABASE := serlo.db
DATABASE_TMP := $(shell mktemp -u)

OUTPUT_DIR := out
INDEX_HTML := $(OUTPUT_DIR)/index.html

TARGETS := $(DATABASE) $(DATABSE_TMP) $(INDEX_HTML)

.PHONY: test $(TARGETS)

all: $(TARGETS)

$(DATABASE_TMP):
	$(PYTHON) highrise_importer.py 'sqlite:///$@'

$(DATABASE): $(DATABASE_TMP)
	mv '$<' '$@'

$(INDEX_HTML): $(OUTPUT_DIR)
	$(PYTHON) create_team_report.py 'sqlite:///$(DATABASE)' \
		'$(TEMPLATE)' > '$@'

$(OUTPUT_DIR):
	mkdir '$@'

test:
	$(PYTHON) -m nose --with-doctest serlo tests
