from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)

class Company(base):
    __tablename__ = "company"

    username = Column("username",primary_key=True)
    companyName= Column("companyName",unique=True)
    email = Column("email",unique=True)
    tel = Column("tel",unique=True)
    type = Column("type",unique=False)