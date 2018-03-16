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

def generate_persons():
    """Helper function for creating persons of type `Person`."""
    email1 = Email(address="hello@example.com")
    email2 = Email(address="My man")
    email3 = Email(address="")

    phone1 = PhoneNumber(number="1")
    phone2 = PhoneNumber(number="2")
    phone3 = PhoneNumber(number="3")

    return (Person(first_name="Markus", last_name="Miller",
                   emails=[email1], phone_numbers=[phone1]),
            Person(first_name="Yannick", last_name="Müller",
                   emails=[email2, email3], phone_numbers=[phone2, phone3]),
            Person(first_name="", last_name="", emails=[], phone_numbers=[]),
            email1, email2, email3, phone1, phone2, phone3)

class TestPerson(TestCase):
    """Testcases for model `Person`."""
    # pylint: disable=too-many-instance-attributes

    def setUp(self):
        self.person1, self.person2, self.person3, \
                self.email1, self.email2, self.email3, \
                self.phone1, self.phone2, self.phone3 = generate_persons()

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

    def test_attribute_emails(self):
        """Testcase for attribute `Person.emails`."""
        self.assertListEqual([x.address for x in self.person1.emails],
                             [self.email1.address])
        self.assertListEqual([x.address for x in self.person2.emails],
                             [self.email2.address, self.email3.address])
        self.assertListEqual(self.person3.emails, [])

    def test_attribute_phone_numbers(self):
        """Testcase for attribute `Person.phone_numbers`."""
        self.assertListEqual([x.number for x in self.person1.phone_numbers],
                             [self.phone1.number])
        self.assertListEqual([x.number for x in self.person2.phone_numbers],
                             [self.phone2.number, self.phone3.number])
        self.assertListEqual(self.person3.phone_numbers, [])

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
    # pylint: disable=too-many-instance-attributes

    def setUp(self):
        self.database = SerloDatabase("sqlite:///:memory:")
        self.person1, self.person2, self.person3, \
                self.email1, self.email2, self.email3, \
                self.phone1, self.phone2, self.phone3 = generate_persons()

        self.persons = [self.person1, self.person2, self.person3]

    def test_storing_nothing(self):
        """Testcase when nothing is stored."""
        self.assertListEqual(list(self.database.persons), [])

        self.database.add_all([])

        self.assertListEqual(list(self.database.persons), [])

    def test_attribute_persons(self):
        """Testcase for storing persons to `SerloDatabase`."""
        self.database.add_all(self.persons)

        stored_persons = set(self.database.persons)

        self.assertSetEqual(set(self.persons), stored_persons)

        for person in self.persons:
            self.assertIsNotNone(person.id)
            self.assertGreater(person.id, 0)

            other = next(x for x in stored_persons if person.id == x.id)

            self.assertIsNotNone(other)
            self.assertEqual(person.first_name, other.first_name)
            self.assertEqual(person.last_name, other.last_name)
            self.assertSetEqual(set(e.address for e in person.emails),
                                set(e.address for e in other.emails))
            self.assertSetEqual(set(p.number for p in person.phone_numbers),
                                set(p.number for p in other.phone_numbers))
