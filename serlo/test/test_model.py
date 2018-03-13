"""Tests for the modul `serlo.model`."""

from abc import ABC, abstractmethod
from unittest import TestCase

from serlo.model import Email

class TestGenericModel(TestCase):
    """Generic tests for the models."""

    def setUp(self):
        self.models = [Email]

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

    def test_model_initialization(self):
        """Test Initialization of a model with several specs and check whether
        attributes are set properly."""
        for spec in self.specs:
            obj = self.cls(**spec)

            for name, value in spec.items():
                self.assertEqual(getattr(obj, name), value)

class TestEmail(ModelTest, TestCase):
    """Testcases for the model `Email`."""
    specs = [
        {"address": "hello@example.org"},
        {"address": "not-an-email"},
        {"address": ""},
    ]

    cls = Email

# ModelTest shall not be tested (see https://stackoverflow.com/a/43353680 )
del ModelTest
