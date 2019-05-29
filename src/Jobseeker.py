from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship


base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)

class Jobseeker(base):
    __tablename__ = "jobseeker"

    username = Column("username",primary_key=True)
    fname = Column("fname",unique=False)
    surname = Column("surname",unique=False)
    email = Column("email",unique=False)
    major = Column("major",unique=False)
    lang = Column("lang",unique=False)
    age = Column("age",unique=False)
    tel = Column("tel",unique=False)