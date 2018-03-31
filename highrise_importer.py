"""Imports contact informations from Highrise into a local database."""

import os
import sys

TOKEN_VARIABLE = "HIGHRISE_API_TOKEN"

def run_script():
    """Executes this script."""
    try:
        api_token = os.environ[TOKEN_VARIABLE]
    except KeyError:
        sys.exit(f"Error: Environment Variable {TOKEN_VARIABLE} not defined.")

if __name__ == "__main__":
    run_script()
