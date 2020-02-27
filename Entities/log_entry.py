from sqlalchemy import Table, MetaData, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from Entities import Base
import datetime

class LogEntry(Base):
    __tablename__="Logs"
    id = Column(Integer, primary_key=True)
    level = Column(String)
    message = Column(String)
    datetime = Column(DateTime)

    def __init__(self, level, message):
        self.level = level
        self.message = message
        self.datetime = datetime.datetime.now()


    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.datetime.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])
