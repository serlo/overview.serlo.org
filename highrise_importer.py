"""Imports contact informations from Highrise into a local database."""

import os
import sys

from serlo.model import SerloDatabase, Email

TOKEN_VARIABLE = "HIGHRISE_API_TOKEN"

def parse_email(xml):
    """Parse emails defined by XML specification `xml`."""
    address_xml = xml.find("address")

    assert address_xml is not None

    address = address_xml.text

    return Email(address=address if address is not None else "")

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
