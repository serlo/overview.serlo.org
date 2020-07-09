PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)
TEMPLATE := template.html

DATABASE := serlo.db
DATABASE_TMP := $(shell mktemp -u)

OUTPUT_DIR := out
INDEX_HTML := $(OUTPUT_DIR)/index.html
FAVICON := $(OUTPUT_DIR)/favicon.ico
CSS := $(OUTPUT_DIR)/styles.css
JAVASCRIPT := $(OUTPUT_DIR)/script.js

TARGETS := $(DATABASE) $(INDEX_HTML) $(FAVICON) $(CSS) $(JAVASCRIPT)

.PHONY: test $(TARGETS)

all: $(TARGETS)

$(DATABASE_TMP):
	$(PYTHON) highrise_importer.py 'sqlite:///$@'

$(DATABASE): $(DATABASE_TMP)
	mv '$<' '$@'

$(FAVICON): $(OUTPUT_DIR)
	curl -s 'https://de.serlo.org/favicon.ico' > '$@'

$(CSS): $(OUTPUT_DIR)
	curl -s 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css' > '$@'
	curl -s 'https://cdn.datatables.net/v/dt/jq-3.3.1/dt-1.10.21/r-2.2.5/datatables.min.css' >> '$@'

$(JAVASCRIPT): $(OUTPUT_DIR)
	curl -s 'https://code.jquery.com/jquery-3.5.1.min.js' > '$@'
	curl -s 'https://cdn.datatables.net/v/dt/jq-3.3.1/dt-1.10.21/r-2.2.5/datatables.min.js' >> '$@'

$(INDEX_HTML): $(OUTPUT_DIR)
	$(PYTHON) create_team_report.py 'sqlite:///$(DATABASE)' \
		'$(TEMPLATE)' > '$@'

$(OUTPUT_DIR):
	mkdir '$@'

test:
	$(PYTHON) -m nose --with-doctest serlo tests
