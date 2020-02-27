from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from Entities import Base


class LogEntry(Base):
    level = Column(String)
    message = Column(String)
    datetime = Column(DateTime)
    