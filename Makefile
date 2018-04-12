PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)
TEMPLATE := report.html

DATABASE := serlo.db
DATABASE_TMP := $(shell mktemp -u)

OUTPUT_DIR := out
INDEX_HTML := $(OUTPUT_DIR)/index.html
FAVICON := $(OUTPUT_DIR)/favicon.ico

TARGETS := $(DATABASE) $(DATABSE_TMP) $(INDEX_HTML) $(FAVICON)

.PHONY: test $(TARGETS)

all: $(TARGETS)

$(DATABASE_TMP):
	$(PYTHON) highrise_importer.py 'sqlite:///$@'

$(DATABASE): $(DATABASE_TMP)
	mv '$<' '$@'

$(FAVICON):
	curl -s 'https://de.serlo.org/favicon.ico' > '$@'

$(INDEX_HTML): $(OUTPUT_DIR)
	$(PYTHON) create_team_report.py 'sqlite:///$(DATABASE)' \
		'$(TEMPLATE)' > '$@'

$(OUTPUT_DIR):
	mkdir '$@'

test:
	$(PYTHON) -m nose --with-doctest serlo tests
