from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)
class Account(base):
    __tablename__ = "userTest"

    username = ""
    password = ""

class UserAcc(Account):
    __tablename__ = "seekerLogin"

    username = Column("username",primary_key=True)
    password = Column("password",unique=False)

class CompanyAcc(Account):
    __tablename__ = "companyLogin"
    username = Column("username", primary_key=True)
    password = Column("password", unique=False)

