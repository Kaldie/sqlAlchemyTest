import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Entities import Base


class MSSql(object):
    Session = sessionmaker()

    def __init__(self):
        self.__engine = None
        self.__session = None
        
        load_dotenv()
        self.__user = os.getenv('USER', None)
        self.__password = os.getenv('PASSWORD', None)
        self.__host = os.getenv('HOST', "localhost")

    def create_engine(self):
        connectionString = 'mssql+pymssql://{user}:{password}@{host}/master'.format(user=self.__user, password=self.__password, host=self.__host)
        self.__engine = create_engine(connectionString, echo=False)
        self.__engine.connect()
        return self.__engine

    def getSession (self):
        if self.__session:
            return self.__session()

        if not self.__engine:
            self.create_engine()

        self.__session = sessionmaker(bind=self.__engine)
        

        print("lala", self.__session)
        return self.__session()

    def updateDatabase(self):
        if not self.__engine:
            self.create_engine()
        Base.metadata.create_all(self.__engine)

if __name__ =="__main__":
    MSSql().create_engine()
