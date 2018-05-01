"""Object relational mapping for Serlo entities."""

import enum

from abc import abstractmethod
from collections.abc import Sequence, Set, Hashable

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, \
                       Table, Enum
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import sessionmaker, relationship

def _hash(obj):
    """Computes the hash value of `obj`. This function expands the domain of
    the builtin function `hash()` to sets and lists."""
    if isinstance(obj, tuple):
        obj = tuple(_hash(x) for x in obj)

    if not isinstance(obj, Hashable):
        if isinstance(obj, Set):
            obj = tuple(sorted(_hash(x) for x in obj))
        elif isinstance(obj, Sequence):
            obj = tuple(_hash(x) for x in obj)

    return hash(obj)

class _SerloEntity(object):
    """Base class of all models."""
    # pylint: disable=too-few-public-methods

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower() # pylint: disable=no-member

    id = Column(Integer, primary_key=True)

    @property
    @abstractmethod
    def _properties(self):
        """Returns all attributes of this object as a tuple which are used
        for equality testing."""
        raise NotImplementedError()

    def __eq__(self, other):
        # pylint: disable=protected-access
        return other is not None and isinstance(other, self.__class__) \
                                 and self.id == other.id \
                                 and self._properties == other._properties

    def __hash__(self):
        return _hash((self.id, self._properties))

    def __repr__(self):
        return self.__class__.__name__ + repr(self._properties)

_SerloEntity = declarative_base(cls=_SerloEntity) #pylint: disable=invalid-name

class Email(_SerloEntity):
    """Model of an email contact."""
    # pylint: disable=too-few-public-methods

    address = Column(String)
    person_id = Column(Integer, ForeignKey("person.id"))
    location = Column(String)

    @property
    def _properties(self):
        return (self.address, self.location)

class PhoneNumber(_SerloEntity):
    """Model of a phone number."""
    # pylint: disable=too-few-public-methods

    number = Column(String)
    person_id = Column(Integer, ForeignKey("person.id"))

    @property
    def _properties(self):
        return (self.number,)

_WorkingUnitParticipants = Table( # pylint: disable=invalid-name
    "working_unit_participants", _SerloEntity.metadata,
    Column("working_unit_id", Integer, ForeignKey("workingunit.id")),
    Column("person_id", Integer, ForeignKey("person.id")))

class Person(_SerloEntity):
    """Model of a person working at Serlo."""
    # pylint: disable=too-few-public-methods

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    emails = relationship("Email")
    phone_numbers = relationship("PhoneNumber")
    managing_units = relationship("WorkingUnit",
                                  back_populates="person_responsible")
    participating_units = relationship("WorkingUnit",
                                       back_populates="participants",
                                       secondary=_WorkingUnitParticipants)
    mentor_id = Column(Integer, ForeignKey("person.id"))
    mentor = relationship("Person", remote_side=[id])
    mentees = relationship("Person", back_populates="mentor")

    @property
    def _properties(self):
        return (self.first_name, self.last_name, self.emails,
                self.phone_numbers)

    @property
    def name(self):
        """Returns the full name of the person.

        >>> p = Person(first_name="Markus", last_name="Miller")
        >>> p.name
        'Markus Miller'
        """
        return self.first_name + " " + self.last_name

    @property
    def work_emails(self):
        """Returns a list of all emails of a person with location 'work'."""
        return [email for email in self.emails if email.location == "Work"]

class UnitType(enum.Enum):
    """Typo of an working unit."""
    project = 1
    support_unit = 2

class UnitStatus(enum.Enum):
    """Status of a working unit."""
    perfect = 1
    ok = 2
    problems = 3

    def __str__(self):
        if self == UnitStatus.perfect:
            return "perfect"
        elif self == UnitStatus.ok:
            return "ok"
        elif self == UnitStatus.problems:
            return "problems"

        raise ValueError("status not known")

class WorkingUnit(_SerloEntity):
    """Model for a working unit."""
    # pylint: disable=too-few-public-methods

    name = Column(String)
    description = Column(String)
    unit_type = Column(Enum(UnitType))
    status = Column(Enum(UnitStatus))
    person_responsible_id = Column(Integer, ForeignKey("person.id"))
    person_responsible = relationship("Person",
                                      back_populates="managing_units",
                                      foreign_keys=[person_responsible_id])
    participants = relationship("Person", back_populates="participating_units",
                                secondary=_WorkingUnitParticipants)
    overview_document = Column(String)

    @property
    def _properties(self):
        return (self.name, self.description, self.unit_type,
                self.person_responsible, self.participants,
                self.overview_document, self.status)

    @property
    def members(self):
        """Returns list of all persons working in this unit (person responsible
        and participants)."""
        return [self.person_responsible] + self.participants

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
        """Returns all stored persons."""
        return self._session.query(Person)

    @property
    def working_units(self):
        """Returns all working units."""
        return self._session.query(WorkingUnit)

    @property
    def projects(self):
        """Returns all active projects."""
        return [p for p in self.working_units
                if p.unit_type == UnitType.project]

    @property
    def support_units(self):
        """Returns all active support units."""
        return [p for p in self.working_units
                if p.unit_type == UnitType.support_unit]
