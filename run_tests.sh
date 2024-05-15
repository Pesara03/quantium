#!/bin/bash

# Activate the project virtual environment
source venv/bin/activate

# Execute the test suite
pytest test_styled_dash.py

# Check the exit code of pytest
if [ $? -eq 0 ]; then
  # Tests passed, return exit code 0
  exit 0
else
  # Tests failed, return exit code 1
  exit 1
fi
