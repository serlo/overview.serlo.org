"""Object relational mapping for Serlo entities."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr, declarative_base

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
