from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)
class Account(base):
    __tablename__ = "userTest"

    id = Column("userid", primary_key=True)
    name = Column("name", String, unique=False)
    age = Column("age", Integer, unique=False)

class UserAcc(base):
    __tablename__ = "seekerLogin"

    username = Column("username",primary_key=True)
    password = Column("password",unique=False)

class CompanyAcc(base):
    __tablename__ = "companyLogin"
    username = Column("username", primary_key=True)
    password = Column("password", unique=False)

