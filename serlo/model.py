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
        self._session = sessionmaker(bind=self._engine)()

        Base.metadata.create_all(self._engine)
