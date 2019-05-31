from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)


class Job(base):
    __tablename__ = "job"


    companyName = Column("companyName",primary_key=True)
    jobName = Column("jobName",primary_key=True)
    salary = Column("salary",unique=False)
    ShortDescription = Column("Shortdescription",unique=False)
    eduLevel = Column("eduLevel",unique=False)
    field = Column("Field",unique=False)
    exp = Column("exp",unique=False)


class Education(base):
    __tablename__ = "education"

    username = Column("username", primary_key=True)
    field = Column("field", primary_key=True)
    degree = Column("degree", primary_key=True)
    major = Column("major", unique=False)
    university = Column("university", unique=False)


