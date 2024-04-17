# Targets
.PHONY: launchlocal initvenv dependencies

# Configurations
PYTHON_VERSION            := 3.10

# Project configuration
WORKDIR                   := .
ENVIRONMENT_DIR           := environment

# Requirements
REQUIRED_PYTHON_PACKAGES      := $(ENVIRONMENT_DIR)/requirements.txt

# Venv virtual environment config
VENV_DIR                      := $(WORKDIR)/.venv

# Detect the OS
ifeq ($(findstring MINGW64, '$(shell uname)'), MINGW64)
        PYTHON_CMD              := python
        PIP                     := $(VENV_DIR)/Scripts/pip
        ACTIVATE_CMD            := source $(VENV_DIR)/Scripts/activate
else ifeq ('$(OS)', 'Windows_NT')
        PYTHON_CMD              := python
        PIP                     := $(VENV_DIR)/Scripts/pip
        ACTIVATE_CMD            := call $(VENV_DIR)/Scripts/activate.bat
else
        PYTHON_CMD              := python3.10
        PIP                     := $(VENV_DIR)/bin/pip
        ACTIVATE_CMD            := source $(VENV_DIR)/bin/activate
endif


# Initialize the virtual environment Venv
initvenv:
	$(PYTHON_CMD) -m venv $(VENV_DIR)
	@echo "To activate this environment in the current OS, use"
	@echo "-                             -"
	@echo "     $$ $(ACTIVATE_CMD)"
	@echo "-                             -"

dependencies:
	pip install -r $(REQUIRED_PYTHON_PACKAGES)

launchlocal:
	$(PYTHON_CMD) ./furnitureCount.py --floor_plan_file_path rooms
