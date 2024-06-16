PYTHON = python

VENV_DIR = venv

REQUIREMENTS = requirements.txt

SCRIPT = api-testing.py

$(VENV_DIR)/bin/activate: $(REQUIREMENTS)
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)

install: $(VENV_DIR)/bin/activate

run: install
	$(VENV_DIR)/bin/$(PYTHON) $(SCRIPT)

clean:
	rm -rf $(VENV_DIR)

