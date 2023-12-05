from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *


Base = declarative_base()


class Host(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fully_qualified_domain_name = Column(String)
    boot_disk_health_status = Column(String)
    boot_disk_model = Column(String)
    boot_disk_capacity_gib = Column(Integer)
    boot_disk_free_space_gib = Column(Integer)
    boot_disk_free_space_ratio = Column(Float)
    total_non_system_capacity_gib = Column(Integer)
    total_non_system_free_space_gib = Column(Integer)
    total_non_system_free_space_ratio = Column(Float)
    total_disk_capacity_gib = Column(Integer)
    total_disk_free_space_gib = Column(Integer)
    total_disk_free_space_ratio = Column(Float)
    cpu_model = Column(String)
    cpu_arch = Column(String)
    total_ram_mb = Column(Integer)
    cpu_count = Column(Integer)
    os_build = Column(String)
    os_version = Column(String)
    os_arch = Column(String)
    bios_serial_number = Column(String)
    chassis_serial_number = Column(String)
    cpu_frequency = Column(Float)
    device_model = Column(String)
    device_manufacturer = Column(String)
    device_pid = Column(String)
    device_product_version = Column(String)
    device_type = Column(String)
    device_uuid = Column(String)
    distinguished_name = Column(String)
    last_seen = Column(String)
    last_boot_duration = Column(Integer)
    users = relationship()
    network_cards = []
    ip_addresses = []
    disks = []

    def __init__(self):
        super().__init__()
