from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.orm import relationship

from Entities import Base
from Entities.address import Address

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)

    addresses = relationship("Address", order_by=Address.id, back_populates="customer")
    
    def __init__(self,firstName, lastName):
        self.firstName =firstName
        self.lastName = lastName

    def addAddres(self, address):
        self.addresses.append(address)

    def __repr__(self):
        return "<Customer(firstName={}, lastName={}, addresses={}".format(self.firstName, self.lastName, self.addresses)