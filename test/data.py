"""This module contains example data for testing."""

from serlo.model import Email

def generate_emails():
    """Returns examples of emails."""
    return [Email(address="hello@example.org"),
            Email(address="some-string-with-ü"),
            Email(address="")]

def generate_email_specs():
    """Returns XML specifications of emails corresponding to the results of
    `emails()`."""
    return ["""<email-address>
                <address>hello@example.org</address>
                <id type="integer">161561239</id>
                <location>Home</location>
               </email-address>""",
            """<email-address>
                <address>some-string-with-ü</address>
                <id type="integer">34567</id>
                <location>Work</location>
               </email-address>""",
            """<email-address><address /></email-address>"""]
