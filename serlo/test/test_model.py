"""Tests for the modul `serlo.model`."""

from abc import ABC, abstractmethod
from unittest import TestCase

from serlo.model import Email, Person, PhoneNumber, SerloDatabase

# pylint: disable=missing-docstring

def generate_specs(params, list_values):
    """Helper function for creating model specifications."""
    return [dict(zip(params, values)) for values in list_values]

class TestGenericModel(TestCase):
    """Generic tests for the models."""

    def setUp(self):
        self.models = [Person]

    def test_attr_tablename(self):
        """Test: Each model needs to have the attribute `__tablename__`."""
        for cls in self.models:
            self.assertEqual(cls.__tablename__, cls.__name__.lower())

class ModelTest(ABC, TestCase):
    """Base class for tests of a model."""

    @property
    @abstractmethod
    def specs(self):
        """List of specifications of different model objects."""
        raise NotImplementedError()

    @property
    @abstractmethod
    def cls(self):
        """Class of the model."""
        raise NotImplementedError()

    def create_entity(self, spec):
        """Creates an entity of type `self.cls` based on the given
        specification."""
        return self.cls(**spec)

    def setUp(self):
        self.database = SerloDatabase("sqlite:///:memory:")

    def test_model_initialization(self):
        """Test Initialization of a model with several specs and check whether
        attributes are set properly."""
        for spec in self.specs:
            obj = self.create_entity(spec)

            for name, value in spec.items():
                self.assertEqual(getattr(obj, name), value)

            # Default value of `id` is None
            self.assertIsNone(obj.id, None)

    def test_add_objects_to_database(self):
        """Tests whether objects can be saved inside the database."""
        objects = [self.create_entity(spec) for spec in self.specs]

        self.database.add_all(objects)

        # pylint: disable=protected-access
        session = self.database._sessionmaker()

        self.assertSetEqual(set(objects), set(session.query(self.cls)))

        # saved objects need to have an id
        for obj in objects:
            self.assertIsNotNone(obj.id)
            self.assertGreater(obj.id, 0)

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

class TestPerson(ModelTest, TestCase):
    """Testcases for model `Person`."""
    specs = generate_specs(
        ("first_name", "last_name"),
        [("Hello", "World"), ("Markus", "Lukas"), ("", "abc")]
    )

    cls = Person

    def test_attribute_name(self):
        """Testcase for attribute `Person.name`."""
        names = [self.create_entity(spec).name for spec in self.specs]

        self.assertListEqual(names, ["Hello World", "Markus Lukas", " abc"])

class TestSerloDatabase(TestCase):
    """Testcases for the class `SerloDatabase`."""

    def test_serlo_database_init(self): # pylint: disable=no-self-use
        """Test initialization of `SerloDatabase`."""
        SerloDatabase("sqlite:///:memory:")

# ModelTest shall not be tested (see https://stackoverflow.com/a/43353680 )
del ModelTest
