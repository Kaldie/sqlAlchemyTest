from Configuration.MSSql import MSSql 
from Entities.customer import Customer
from Entities.address import Address

from Entities import Base

import logging
import Logging

if __name__ =="__main__":
    # MSSql().updateDatabase()
    # session = MSSql().getSession()

    # ed_customer = Customer("ruud","lala")
    # ed_customer.addAddres(Address("lala", 10))
    # ed_customer.addAddres(Address("lala", 11))
    
    logging.getLogger("dblogger").critical("magic magic")

    # session.add(ed_customer)
    # session.commit()
