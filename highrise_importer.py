"""Imports contact informations from Highrise into a local database."""

import os
import sys

from serlo.model import SerloDatabase, Email, PhoneNumber

TOKEN_VARIABLE = "HIGHRISE_API_TOKEN"

def xml_text(xml):
    """Returns the inner text of the XML element `xml`. In case it doesn't
    contain an inner text an empty string is returned."""
    return str.join('', xml.itertext())

def parse_email(xml):
    """Parse emails defined by XML specification `xml`."""
    address_xml = xml.find("address")

    assert address_xml is not None

    return Email(address=xml_text(address_xml))

def parse_phone_number(xml):
    """Parse phone number defined by XML specification `xml`."""
    number_xml = xml.find("number")

    assert number_xml is not None

    return PhoneNumber(number=xml_text(number_xml))

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
