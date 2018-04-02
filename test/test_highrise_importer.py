"""Testsuite for python script `highrise_importer.py`."""

import os
import subprocess

from unittest import TestCase

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

    def test_passing_arguments(self):
        """Testcase for calling the script without set arguments."""
        returncode, out, err = run_command("python highrise_importer.py")

        self.assertEqual(returncode, 1)
        self.assertEqual(out, "")
        self.assertEqual(err, "Error: No database file specified as " + \
                              "first argument.\n")
