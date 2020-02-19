from Configuration.MSSql import MSSql 
from Entities.customer import Customer
from Entities.address import Address

from Entities import Base

if __name__ =="__main__":
    MSSql().updateDatabase()
    session = MSSql().getSession()
    print(Customer)
    ed_customer = Customer("ruud","lala")
    session.add(ed_customer)
    session.commit()