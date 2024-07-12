# Justfile for initializing the WBM Notifier project

# Define a variable for the virtual environment directory
VENV_DIR := "venv"

# Recipe to install pre-commit hooks
install-hooks:
    ./{{VENV_DIR}}/bin/pip install .[dev]
    ./{{VENV_DIR}}/bin/pip install .[dev]
    ./{{VENV_DIR}}/bin/pre-commit install

# Recipe to create a virtual environment
init:
    python3.12 -m venv {{VENV_DIR}}
    ./{{VENV_DIR}}/bin/pip install --upgrade pip
    ./{{VENV_DIR}}/bin/pip install -e .
    ./{{VENV_DIR}}/bin/pip install pre-commit
    ./{{VENV_DIR}}/bin/pre-commit install

# Recipe to activate the virtual environment
activate:
    @echo "Run the following command to activate the virtual environment:"
    @echo "source {{VENV_DIR}}/bin/activate"

# Recipe to install dependencies
install-deps:
    ./{{VENV_DIR}}/bin/pip install -r requirements.txt

# Recipe to install the package as editable in the virtual environment
install-editable:
    ./{{VENV_DIR}}/bin/pip install -e .

# Recipe to run the wbm-notifier
run:
    ./{{VENV_DIR}}/bin/python -m wbm_notifier

# Recipe to run tests
test:
    ./{{VENV_DIR}}/bin/pip install .[dev]
    ./{{VENV_DIR}}/bin/pytest tests
