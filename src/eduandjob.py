from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)


class Job(base):
    __tablename__ = "jobs"

    companyName = Column("companyName",primary_key=True)
    jobName = Column("jobName",primary_key=True)
    salary = Column("salary",unique=False)
    sdesc = Column("sdesc",unique=False)
    degree = Column("degree",unique=False)
    field = Column("Field",unique=False)
    exp = Column("exp",unique=False)
    position = Column("position",unique=False)


class Education(base):
    __tablename__ = "education"

    username = Column("username", primary_key=True)
    field = Column("field", primary_key=True)
    degree = Column("degree", primary_key=True)
    major = Column("major", unique=False)
    university = Column("university", unique=False)


class Address(base):
    __tablename__ = "companyAddr"

    companyName = Column("companyName",primary_key=True)
    number = Column("number",unique=False)
    soi = Column("soi", unique=False)
    street = Column("street", unique=False)
    district = Column("district", unique=False)
    city = Column("city", unique=False)
    province = Column("province", unique=False)
    zipcode = Column("zipcode", unique=False)
