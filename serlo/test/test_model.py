"""Tests for the modul `serlo.model`."""

from unittest import TestCase

from serlo.model import Email, Person, PhoneNumber, SerloDatabase

class TestEmail(TestCase):
    """Testcases for the model `Email`."""

    def setUp(self):
        self.email1 = Email(address="hello@example.org")
        self.email2 = Email(address="")
        self.email3 = Email(address="not-an-email")

    def test_attribute_tablename(self):
        """Testcase for attribute `Email.__tablename__`."""
        self.assertEqual(Email.__tablename__, "email")

    def test_attribute_id(self):
        """Testcase for attribute `Email.id`."""
        self.assertIsNone(self.email1.id)
        self.assertIsNone(self.email2.id)
        self.assertIsNone(self.email3.id)

    def test_attribute_address(self):
        """Testcase for attribute `Email.address`."""
        self.assertEqual(self.email1.address, "hello@example.org")
        self.assertEqual(self.email2.address, "")
        self.assertEqual(self.email3.address, "not-an-email")

class TestPhoneNumber(TestCase):
    """Testcases for the model `PhoneNumber`."""

    def setUp(self):
        self.number1 = PhoneNumber(number="+49017867")
        self.number2 = PhoneNumber(number="0178645389")
        self.number3 = PhoneNumber(number="")

    def test_attribute_tablename(self):
        """Testcase for attribute `__tablename__`."""
        self.assertEqual(PhoneNumber.__tablename__, "phonenumber")

    def test_attribute_id(self):
        """Testcase for attribute `PhoneNumber.id`."""
        self.assertIsNone(self.number1.id)
        self.assertIsNone(self.number2.id)
        self.assertIsNone(self.number3.id)

    def test_attribute_number(self):
        """Testcase for attribute `PhoneNumber.number`."""
        self.assertEqual(self.number1.number, "+49017867")
        self.assertEqual(self.number2.number, "0178645389")
        self.assertEqual(self.number3.number, "")

class TestPerson(TestCase):
    """Testcases for model `Person`."""

    def setUp(self):
        self.person1 = Person(first_name="Markus", last_name="Miller")
        self.person2 = Person(first_name="Yannick", last_name="Müller")
        self.person3 = Person(first_name="", last_name="")

    def test_attribute_id(self):
        """Testcase for attribute `Person.id`."""
        self.assertIsNone(self.person1.id)
        self.assertIsNone(self.person2.id)

    def test_attribute_tablename(self):
        """Testcase for attribute `Person.__tablename__`."""
        self.assertEqual(Person.__tablename__, "person")

    def test_attribute_first_name(self):
        """Testcase for attribute `Person.first_name`."""
        self.assertEqual(self.person1.first_name, "Markus")
        self.assertEqual(self.person2.first_name, "Yannick")
        self.assertEqual(self.person3.first_name, "")

    def test_attribute_last_name(self):
        """Testcase for attribute `Person.last_name`."""
        self.assertEqual(self.person1.last_name, "Miller")
        self.assertEqual(self.person2.last_name, "Müller")
        self.assertEqual(self.person3.last_name, "")

    def test_attribute_name(self):
        """Testcase for attribute `Person.name`."""
        self.assertEqual(self.person1.name, "Markus Miller")
        self.assertEqual(self.person2.name, "Yannick Müller")
        self.assertEqual(self.person3.name, " ")

class TestSerloDatabase(TestCase):
    """Testcases for the class `SerloDatabase`."""

    def setUp(self):
        self.database = SerloDatabase("sqlite:///:memory:")

    def test_serlo_database_init(self): # pylint: disable=no-self-use
        """Test initialization of `SerloDatabase`."""
        SerloDatabase("sqlite:///:memory:")
