from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Entities import Base

class MSSql(object):
    Session = sessionmaker()

    def __init__(self):
        self.__engine = None
        self.__session = None

    def create_engine(self):
        self.__engine = create_engine('mssql+pymssql://sa:magic11!@localhost/master', echo=True)
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