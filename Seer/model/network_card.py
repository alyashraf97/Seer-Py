from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *


Base = declarative_base()


class NetworkCard(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    ip_address = Column(String)
    mtu = Column(Integer)
    physical_address = Column(String)
    gateway_address = Column(String)
    vlan_id = Column(Integer)
    primary_dns = Column(String)
    secondary_dns = Column(String)
    tertiary_dns = Column(String)
    state = Column(String)
    iana_code = Column(String)
    rx_statistics = Column(BigInteger)
    tx_statistics = Column(BigInteger)

    def __init__(self):
        super().__init__()

