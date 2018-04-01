"""Imports contact informations from Highrise into a local database."""

import os
import sys

from serlo.model import SerloDatabase

TOKEN_VARIABLE = "HIGHRISE_API_TOKEN"

def run_script():
    """Executes this script."""
    try:
        database_file = sys.argv[1]
    except IndexError:
        sys.exit("Error: No database file specified as first argument.")

    try:
        api_token = os.environ[TOKEN_VARIABLE]
    except KeyError:
        sys.exit(f"Error: Environment Variable {TOKEN_VARIABLE} not defined.")

    database = SerloDatabase(database_file)

if __name__ == "__main__":
    run_script()
