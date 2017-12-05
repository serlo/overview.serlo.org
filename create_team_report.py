import os
import sys
import xml.etree.ElementTree as ET

from collections import namedtuple
from functools import lru_cache, reduce

import jinja2
import requests

PROJECT_ID = "6436430"
SUPPORT_UNIT_ID="4849968"

TOKEN_VARIABLE = "HIGHRISE_API_TOKEN"

def text(xml):
    return xml.text

def xml_get(xml, key):
    if xml is None:
        return None
    elif isinstance(key, int):
        return xml[key]
    elif callable(key):
        return key(xml)
    else:
        return xml.find(key)

def query(xml, path):
    return reduce(xml_get, path, xml)

class Person:
    def __init__(self, xml):
        self.first_name = query(xml, ["first-name", text])
        self.last_name = query(xml, ["last-name", text])

        contacts = xml.find("contact-data")

        self.emails = [ query(x, ["address", text]) for x
                        in contacts.find("email-addresses") ]
        self.numbers = [ query(x, ["number", text]) for x
                        in contacts.find("phone-numbers") ]
        self.xml = xml

    @property
    def name(self):
        return self.first_name + " " + self.last_name

    @property
    def email(self):
        try:
            return self.emails[0]
        except IndexError:
            return None

    @property
    def phone_number(self):
        try:
            return self.numbers[0]
        except IndexError:
            return None

class Project:
    def __init__(self, xml):
        self.name = query(xml, ["name", text])
        self.status = query(xml, ["status", text])
        self.description = query(xml, ["background", text])
        self.lama = Person(xml.find("party"))
        self.participants = [ Person(x) for x in xml.find("parties") ]
        self.xml = xml

    @property
    def members(self):
        return [self.lama] + self.participants

class Highrise:
    def __init__(self, project, api_token):
        self.project = project
        self.api_token = api_token

    def api_call(self, endpoint, params={}):
        url = f"https://{self.project}.highrisehq.com/{endpoint}.xml"
        req = requests.get(url, auth=(self.api_token, "_"), params=params)

        return ET.fromstring(req.text)

    @property
    @lru_cache(maxsize=None)
    def deals(self):
        return self.api_call("deals")

    def get_projects_by_category(self, category_id):
        return [ Project(x) for x in self.deals
                 if query(x, ["category-id", text]) == category_id ]

    @property
    def projects(self):
        return self.get_projects_by_category(PROJECT_ID)

    @property
    def support_units(self):
        return self.get_projects_by_category(SUPPORT_UNIT_ID)

    @property
    def members(self):
        params = { "tag_id": "5372644" }

        return [ Person(x) for x in self.api_call("people", params) ]

def error(message):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)

def run_script():
    try:
        api_token = os.environ[TOKEN_VARIABLE]
    except KeyError:
        error(f"Environment Variable {TOKEN_VARIABLE}")

    highrise = Highrise("de-serlo", api_token)

    env = jinja2.Environment(autoescape=True,
                             loader=jinja2.FileSystemLoader("."))

    template = env.get_template("report.html")

    print(template.render(projects=highrise.projects,
                          support_units=highrise.support_units,
                          members=highrise.members))

if __name__ == "__main__":
    run_script()
