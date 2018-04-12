"""Tests for the modul `serlo.model`."""

from unittest import TestCase

from serlo.model import UnitType, Email, Person, PhoneNumber, SerloDatabase, \
                        WorkingUnit
from tests.data import generate_persons, generate_emails, \
                       generate_working_units, generate_phone_numbers

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
    # pylint: disable=too-many-instance-attributes

    def setUp(self):
        self.person1, self.person2, self.person3 = generate_persons()
        self.email1, self.email2, self.email3 = generate_emails()
        self.phone1, self.phone2, self.phone3 = generate_phone_numbers()

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
        self.assertListEqual(self.person1.emails, [self.email1])
        self.assertListEqual(self.person2.emails, [self.email2, self.email3])
        self.assertListEqual(self.person3.emails, [])

    def test_attribute_phone_numbers(self):
        """Testcase for attribute `Person.phone_numbers`."""
        self.assertListEqual(self.person1.phone_numbers, [self.phone1])
        self.assertListEqual(self.person2.phone_numbers,
                             [self.phone2, self.phone3])
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

class TestWorkingUnit(TestCase):
    """Testcases for the class `WorkingUnit`."""

    def setUp(self):
        self.project1, self.project2, \
                self.unit1, self.unit2 = generate_working_units()

        self.person1, self.person2, self.person3 = generate_persons()

    def test_attribute_tablename(self):
        """Test for attribute `WorkingUnit.__tablename__`."""
        self.assertEqual(WorkingUnit.__tablename__, "workingunit")

    def test_attribute_id(self):
        """Test for attribute `WorkingUnit.id`"""
        self.assertIsNone(self.project1.id)
        self.assertIsNone(self.unit1.id)

    def test_attribute_name(self):
        """Test for attribute `WorkingUnit.name`."""
        self.assertEqual(self.project1.name, "project1")
        self.assertEqual(self.project2.name, "")
        self.assertEqual(self.unit1.name, "Support Unit Master")
        self.assertEqual(self.unit2.name, "Another support unit")

    def test_attribute_description(self):
        """Test for attribute `WorkingUnit.description`."""
        self.assertEqual(self.project1.description, "My description")
        self.assertEqual(self.project2.description, "")
        self.assertEqual(self.unit1.description, "A cool unit.")
        self.assertEqual(self.unit2.description, "Hello World")

    def test_attribute_person_responsible(self): # pylint: disable=invalid-name
        """Test for attribute `WorkingUnit.person_responsible`."""
        self.assertEqual(self.project1.person_responsible, self.person1)
        self.assertEqual(self.project2.person_responsible, self.person2)
        self.assertEqual(self.unit1.person_responsible, self.person1)
        self.assertEqual(self.unit2.person_responsible, self.person3)

    def test_attribute_participants(self):
        """Test for attribute `WorkingUnit.participants`."""
        self.assertListEqual(self.project1.participants, [self.person3])
        self.assertListEqual(self.project2.participants, [])
        self.assertListEqual(self.unit1.participants, [self.person2])
        self.assertListEqual(self.unit2.participants,
                             [self.person1, self.person2])

    def test_attribute_members(self):
        """Test for attribute `WorkingUnit.members`."""
        self.assertListEqual(self.project1.members,
                             [self.person1, self.person3])
        self.assertListEqual(self.project2.members, [self.person2])
        self.assertListEqual(self.unit1.members, [self.person1, self.person2])
        self.assertListEqual(self.unit2.members,
                             [self.person3, self.person1, self.person2])

    def test_attribute_unit_type(self): # pylint: disable=invalid-name
        """Test for attribute `WorkingUnit.type`."""
        self.assertEqual(self.project1.unit_type, UnitType.project)
        self.assertEqual(self.project2.unit_type, UnitType.project)
        self.assertEqual(self.unit1.unit_type, UnitType.support_unit)
        self.assertEqual(self.unit2.unit_type, UnitType.support_unit)

    def test_attribute_overview_document(self): # pylint: disable=invalid-name
        """Test for attribute `WorkingUnit.overview_document`"""
        self.assertEqual(self.project1.overview_document, "overview_document")
        self.assertEqual(self.project2.overview_document, "")
        self.assertEqual(self.unit1.overview_document, "http://example.org")
        self.assertEqual(self.unit2.overview_document, "Hello Document")

class TestSerloDatabase(TestCase):
    """Testcases for the class `SerloDatabase`."""
    # pylint: disable=too-many-instance-attributes

    def setUp(self):
        self.database = SerloDatabase("sqlite:///:memory:")
        self.person1, self.person2, self.person3 = generate_persons()[0:3]

        self.persons = [self.person1, self.person2, self.person3]

        self.project1, self.project2, \
                self.unit1, self.unit2 = generate_working_units()[0:4]

        self.units = [self.project1, self.project2, self.unit1, self.unit2]

    def test_storing_nothing(self):
        """Testcase when nothing is stored."""
        self.assertListEqual(list(self.database.persons), [])
        self.assertListEqual(list(self.database.working_units), [])

        self.database.add_all([])

        self.assertListEqual(list(self.database.persons), [])
        self.assertListEqual(list(self.database.working_units), [])

    def test_attribute_persons(self):
        """Testcase for storing persons to `SerloDatabase`."""
        self.database.add_all(self.persons)

        self.assertSetEqual(set(self.database.persons), set(self.persons))

    def test_atttribute_working_units(self):
        """Testcase for storing working units to `SerloDatabase`."""
        self.database.add_all([self.project2, self.project1])
        self.database.add_all([self.unit1, self.unit2])

        self.assertSetEqual(set(self.database.working_units), set(self.units))

    def test_attribute_projects(self):
        """Testcase for accessing all active projects."""
        self.database.add_all([self.project1, self.project2, self.unit1,
                               self.unit2])

        self.assertSetEqual(set(self.database.projects),
                            set([self.project1, self.project2]))

    def test_attribute_support_units(self):
        """Testcase for accessing all active support_units."""
        self.database.add_all([self.project1, self.project2, self.unit1,
                               self.unit2])

        self.assertSetEqual(set(self.database.support_units),
                            set([self.unit1, self.unit2]))
