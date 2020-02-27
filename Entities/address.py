from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Entities import Base


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    streetName = Column(String)
    houseNumber = Column(Integer)
    # houseNumberAppendix = Column(String)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", back_populates="addresses")
    def __init__(self, streetName, houseNumber):
        self.streetName = streetName
        self.houseNumber = houseNumber
        
    def __repr__(self):
        return "<Address(streetname={}, houseNumber={}>".format(self.streetName, self.houseNumber)