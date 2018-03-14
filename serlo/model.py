"""Object relational mapping for Serlo entities."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import sessionmaker

class Base(object):
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
        return self.id if self.id is not None else -1

Base = declarative_base(cls=Base) # pylint: disable=invalid-name

class Email(Base):
    """Model of an email contact."""
    # pylint: disable=too-few-public-methods

    address = Column(String)

class SerloDatabase(object):
    """Class for accessing the stored entities of Serlo and saving new
    entities."""

    def __init__(self, database):
        """Initializes the object. The parameter `database` is a specification
        of the database."""

        self._engine = create_engine(database)
        self._sessionmaker = sessionmaker(bind=self._engine)

        Base.metadata.create_all(self._engine)

    def add_all(self, instances):
        """Adds all entities of the iterator `iterator` to the database."""
        session = self._sessionmaker()

        session.add_all(instances)
        session.commit()
