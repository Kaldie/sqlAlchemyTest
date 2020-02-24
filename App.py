from Configuration.MSSql import MSSql 
from Entities.customer import Customer
from Entities.address import Address

from Entities import Base

if __name__ =="__main__":
    MSSql().updateDatabase()
    session = MSSql().getSession()

    ed_customer = Customer("ruud","lala")
    ed_customer.addAddres(Address("lala", 10))
    ed_customer.addAddres(Address("lala", 11))
    session.add(ed_customer)

    print("HEEEEEEEEEEEEEREEEEEEEEEEEE", ed_customer)

    session.commit()