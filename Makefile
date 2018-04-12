PYTHON := $(shell if which pyenv > /dev/null; \
                 then echo python ; else echo python3 ; fi)
TEMPLATE := report.html

DATABASE := serlo.db
DATABASE_TMP := $(shell mktemp -u)

OUTPUT_DIR := out
INDEX_HTML := $(OUTPUT_DIR)/index.html
FAVICON := $(OUTPUT_DIR)/favicon.ico
CSS := $(OUTPUT_DIR)/styles.css

TARGETS := $(DATABASE) $(INDEX_HTML) $(FAVICON) $(CSS)

.PHONY: test $(TARGETS)

all: $(TARGETS)

$(DATABASE_TMP):
	$(PYTHON) highrise_importer.py 'sqlite:///$@'

$(DATABASE): $(DATABASE_TMP)
	mv '$<' '$@'

$(FAVICON):
	curl -s 'https://de.serlo.org/favicon.ico' > '$@'

$(CSS): $(OUTPUT_DIR)
	curl -s 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css' > '$@'
	curl -s 'https://cdn.datatables.net/1.10.16/css/jquery.dataTables.css' >> '$@'

$(INDEX_HTML): $(OUTPUT_DIR)
	$(PYTHON) create_team_report.py 'sqlite:///$(DATABASE)' \
		'$(TEMPLATE)' > '$@'

$(OUTPUT_DIR):
	mkdir '$@'

test:
	$(PYTHON) -m nose --with-doctest serlo tests
