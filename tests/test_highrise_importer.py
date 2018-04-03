"""Testsuite for python script `highrise_importer.py`."""

import os
import subprocess
import xml.etree.ElementTree as ET

from unittest import TestCase

from highrise_importer import parse_email, parse_phone_number, \
                              xml_text, xml_find
from tests.data import generate_emails, generate_email_specs, \
                       generate_phone_numbers, generate_phone_number_specs

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def run_command(args, env=None):
    """Executes command with the environment `env`. This functions returns the
    return code of the command and the printed `stderr` and `stdout`."""
    if env is None:
        env = {}

    env.update({key: value for key, value in os.environ.items()
                if key.startswith("PYENV") or key == "PATH"})

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

    def test_passing_arguments(self):
        """Testcase for calling the script without arguments."""
        returncode, out, err = run_command("python highrise_importer.py")

        self.assertEqual(returncode, 1)
        self.assertEqual(out, "")
        self.assertEqual(err, "Error: No database file specified as " + \
                              "first argument.\n")
