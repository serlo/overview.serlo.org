"""Testsuite for python script `highrise_importer.py`."""

import os
import subprocess
import xml.etree.ElementTree as ET

from unittest import TestCase

from highrise_importer import parse_email, parse_phone_number, parse_person, \
                              parse_people, parse_working_unit, xml_text, \
                              xml_find, parse_working_units, parse_mentoring, \
                              parse_tag
from tests.data import generate_emails, generate_email_specs, \
                       generate_phone_numbers, generate_phone_number_specs, \
                       generate_persons, generate_person_specs, \
                       generate_people, generate_people_specs, \
                       generate_working_units, generate_working_unit_specs, \
                       generate_person_ids, generate_working_unit_list_spec, \
                       generate_mentoring_spec, generate_tags, \
                       generate_tag_specs

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def run_command(args, env=None):
    """Executes command with the environment `env`. This functions returns the
    return code of the command and the printed `stderr` and `stdout`."""
    result = subprocess.run(args, cwd=ROOT_DIR, env=env,
                            stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, timeout=10, shell=True)

    return (result.returncode, result.stdout.decode("utf-8"),
            result.stderr.decode("utf-8"))

class TestHighriseImporterScript(TestCase):
    """Testsuite for executing the script."""

    def test_xml_text(self):
        """Tests for function `xml_text()`."""
        self.assertEqual(xml_text(ET.fromstring("<a>Hello</a>")), "Hello")
        self.assertEqual(xml_text(ET.fromstring("<a>Hello <b>World</b></a>")),
                         "Hello World")
        self.assertEqual(xml_text(ET.fromstring("<a></a>")), "")
        self.assertEqual(xml_text(ET.fromstring("<a/>")), "")

        with self.assertRaises(TypeError):
            xml_text(None)

    def test_xml_find(self):
        """Tests for function `xml_find()`."""
        xml = ET.fromstring("<a><b><c>1</c></b><d /><e>42</e></a>")

        self.assertEqual(xml_find("b", xml), xml.find("b"))
        self.assertEqual(xml_find("e", xml).text, "42")

        with self.assertRaises(AssertionError):
            xml_find("b", ET.fromstring("<a><c/><d/></a>"))

        with self.assertRaises(AssertionError):
            xml_find("b", ET.fromstring("<a><b><c/></b><b /></a>"))

        with self.assertRaises(AssertionError):
            xml_find("b", ET.fromstring("<a></a>"))

        with self.assertRaises(TypeError):
            xml_find("b", None)

    def test_parse_email(self):
        """Testcase for the function `parse_email()`."""
        specs = [ET.fromstring(x) for x in generate_email_specs()]
        emails = generate_emails()

        self.assertEqual(parse_email(specs[0]), emails[0])
        self.assertEqual(parse_email(specs[1]), emails[1])
        self.assertEqual(parse_email(specs[2]), emails[2])

    def test_parse_phone_number(self):
        """Testcase for the function `parse_phone_number()`."""
        specs = [ET.fromstring(x) for x in generate_phone_number_specs()]
        numbers = generate_phone_numbers()

        self.assertEqual(parse_phone_number(specs[0]), numbers[0])
        self.assertEqual(parse_phone_number(specs[1]), numbers[1])
        self.assertEqual(parse_phone_number(specs[2]), numbers[2])

    def test_parse_tag(self):
        """Testcase for the function `parse_phone_number()`."""
        specs = [ET.fromstring(x) for x in generate_tag_specs()]
        tags = generate_tags()

        self.assertEqual(parse_tag(specs[0]), tags[0])
        self.assertEqual(parse_tag(specs[1]), tags[1])
        self.assertEqual(parse_tag(specs[2]), tags[2])

    def test_parse_person(self):
        """Testcase for the function `parse_person()`."""
        specs = [ET.fromstring(x) for x in generate_person_specs()]
        persons = generate_persons()
        ids = generate_person_ids()

        self.assertEqual(parse_person(specs[0]), (ids[0], persons[0]))
        self.assertEqual(parse_person(specs[1]), (ids[1], persons[1]))
        self.assertEqual(parse_person(specs[2]), (ids[2], persons[2]))

    def test_parse_people(self):
        """Testcase for the function `parse_people()`."""
        specs = [ET.fromstring(x) for x in generate_people_specs()]
        people = generate_people()

        self.assertListEqual(parse_people(specs[0]), people[0])
        self.assertListEqual(parse_people(specs[1]), people[1])
        self.assertListEqual(parse_people(specs[2]), people[2])

    def test_parse_working_unit(self):
        """Testcase for the function `parse_working_unit()`."""
        specs = [ET.fromstring(x) for x in generate_working_unit_specs()]
        units = generate_working_units()
        persons = dict(parse_people(ET.fromstring(generate_people_specs()[0])))

        self.assertEqual(parse_working_unit(specs[0], persons), units[0])
        self.assertEqual(parse_working_unit(specs[1], persons), units[1])
        self.assertEqual(parse_working_unit(specs[2], persons), units[2])
        self.assertEqual(parse_working_unit(specs[3], persons), units[3])

        self.assertIsNone(parse_working_unit(
            ET.fromstring("""<deal>
                              <category-id type="integer">123</category-id>
                             </deal>"""), persons))

    def test_parse_working_units(self):
        """Testcase for the function `parse_working_units()`."""
        units = generate_working_units()
        spec = ET.fromstring(generate_working_unit_list_spec())
        persons = dict(parse_people(ET.fromstring(generate_people_specs()[0])))

        self.assertListEqual(parse_working_units(spec, persons), units)

    def test_parse_mentoring(self):
        """Testcase for the function `parse_mentoring()`."""
        spec = ET.fromstring(generate_mentoring_spec())
        id1, id2, id3 = generate_person_ids()

        self.assertDictEqual(parse_mentoring(spec),
                             {id2: [id1], id3: [id2]})

    def test_passing_arguments(self):
        """Testcase for calling the script without arguments."""
        returncode, out, err = run_command("python highrise_importer.py")

        self.assertEqual(returncode, 1)
        self.assertEqual(out, "")
        self.assertEqual(err.strip(), "Error: No database file specified as " + \
                                      "first argument.")
