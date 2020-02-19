from sqlalchemy import Table, MetaData, Column, Integer, String
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


