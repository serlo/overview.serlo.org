"""Testsuite for python script `highrise_importer.py`."""

import os
import subprocess
import xml.etree.ElementTree as ET

from unittest import TestCase

from highrise_importer import parse_email
from test.data import generate_emails, generate_email_specs

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

    def test_parse_emails(self):
        """Testcase for parsing emails from XML."""
        specs = [ET.fromstring(x) for x in generate_email_specs()]
        emails = generate_emails()

        self.assertEqual(parse_email(specs[0]), emails[0])
        self.assertEqual(parse_email(specs[1]), emails[1])
        self.assertEqual(parse_email(specs[2]), emails[2])

    def test_passing_arguments(self):
        """Testcase for calling the script without set arguments."""
        returncode, out, err = run_command("python highrise_importer.py")

        self.assertEqual(returncode, 1)
        self.assertEqual(out, "")
        self.assertEqual(err, "Error: No database file specified as " + \
                              "first argument.\n")
