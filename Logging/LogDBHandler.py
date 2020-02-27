import datetime
import logging

from Configuration.MSSql import MSSql
from Entities.log_entry import LogEntry

class LogDBHandler(logging.Handler):
    '''
    Customized logging handler that puts logs to the database.
    pymssql required
    '''

    def __init__(self):
        print("here!")
        print(abc)
        logging.Handler.__init__(self)
        self.__mssql = MSSql()

    def emit(self, record):
        self.__mssql = MSSql()
        entry = LogEntry(record.levelname, record.msg.strip().replace('\'','\'\''))
        print("HHHHHHHHHHHEEEEEEEEEEEEEEEEEERRRRRRRRREEEEEEEEEe")
        session = self.__mssql.getSession()
        session.add(entry)
        session.commit()