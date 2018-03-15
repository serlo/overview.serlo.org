"""Tests for the modul `serlo.model`."""

from abc import ABC, abstractmethod
from unittest import TestCase

from serlo.model import Email, Person, PhoneNumber, SerloDatabase

def generate_specs(params, list_values):
    """Helper function for creating model specifications."""
    return [dict(zip(params, values)) for values in list_values]

class TestGenericModel(TestCase):
    """Generic tests for the models."""

    def setUp(self):
        self.models = [Email, Person, PhoneNumber]

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

class TestEmail(ModelTest, TestCase):
    """Testcases for the model `Email`."""
    specs = generate_specs(["address"],
                           [["hello@example.org"], [""], ["not-an-email"]])

    cls = Email

class TestPhoneNumber(ModelTest, TestCase):
    """Testcases for the model `PhoneNumber`."""
    specs = generate_specs(["number"],
                           [["+49017867"], [""], "01781523467"])

    cls = PhoneNumber

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
