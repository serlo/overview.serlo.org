"""Object relational mapping for Serlo entities."""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import sessionmaker, relationship

class _SerloEntity(object):
    """Base class of all models."""
    # pylint: disable=too-few-public-methods

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower() # pylint: disable=no-member

    id = Column(Integer, primary_key=True)

    def __eq__(self, other):
        return other is not None and self.__class__ == other.__class__ \
                                 and self.id == other.id

    def __hash__(self):
        return hash(self.id)

_SerloEntity = declarative_base(cls=_SerloEntity) #pylint: disable=invalid-name

class Email(_SerloEntity):
    """Model of an email contact."""
    # pylint: disable=too-few-public-methods

    address = Column(String)
    person_id = Column(Integer, ForeignKey("person.id"))

class PhoneNumber(_SerloEntity):
    """Model of a phone number."""
    # pylint: disable=too-few-public-methods

    number = Column(String)

class Person(_SerloEntity):
    """Model of a person working at Serlo."""
    # pylint: disable=too-few-public-methods

    first_name = Column(String)
    last_name = Column(String)
    emails = relationship("Email")

    @property
    def name(self):
        """Returns the full name of the person.

        >>> p = Person(first_name="Markus", last_name="Miller")
        >>> p.name
        'Markus Miller'
        """
        return self.first_name + " " + self.last_name

class SerloDatabase(object):
    """Class for accessing the stored entities of Serlo and saving new
    entities."""

    def __init__(self, database):
        """Initializes the object. The parameter `database` is a specification
        of the database."""

        self._engine = create_engine(database)
        self._session = sessionmaker(bind=self._engine)()

        _SerloEntity.metadata.create_all(self._engine)

    def add_all(self, instances):
        """Adds all entities of the iterator `iterator` to the database."""
        self._session.add_all(instances)
        self._session.commit()

    @property
    def persons(self):
        """Returns all stored persons of type `Per"""
        return self._session.query(Person)
