"""Imports contact informations from Highrise into a local database."""

import os
import sys

from serlo.model import SerloDatabase, Email, PhoneNumber, Person

TOKEN_VARIABLE = "HIGHRISE_API_TOKEN"

def xml_text(xml):
    """Returns the inner text of the XML element `xml`. In case it doesn't
    contain an inner text an empty string is returned."""
    if xml is None:
        raise TypeError("xml_text(): XML argument must not be 'None'")

    return str.join('', xml.itertext())

def xml_find(tag_name, xml):
    """Returns the child with tag `tag_name` of the XML element `xml`. It
    throws an `AssertationError` when no or more than one children of the tag
    `tag_name` are defined."""
    if xml is None:
        raise TypeError("xml_text(): XML argument must not be 'None'")

    results = xml.findall(tag_name)

    assert results, f"Child with tag `{tag_name}` not found."
    assert len(results) < 2, f"Too many children with tag `{tag_name}` found."

    return results[0]

def parse_email(xml):
    """Parse emails defined by XML specification `xml`."""
    return Email(address=xml_text(xml_find("address", xml)))

def parse_phone_number(xml):
    """Parse phone number defined by XML specification `xml`."""
    return PhoneNumber(number=xml_text(xml_find("number", xml)))

def parse_person(xml):
    """Parse person defined by XML specification `xml`."""
    contact_data = xml_find("contact-data", xml)

    return (xml_text(xml_find("id", xml)),
            Person(first_name=xml_text(xml_find("first-name", xml)),
                   last_name=xml_text(xml_find("last-name", xml)),
                   emails=[parse_email(e) for e in
                           xml_find("email-addresses", contact_data)],
                   phone_numbers=[parse_phone_number(e) for e in
                                  xml_find("phone-numbers", contact_data)]))
def parse_people(xml):
    """Parse people defined by XML specification `xml`."""
    return [parse_person(e) for e in xml.findall("person", xml)]

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
