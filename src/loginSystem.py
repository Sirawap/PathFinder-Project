from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from 

base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)

class LoginSystem():
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def createCompany(self):
        Session = sessionmaker(bind = self.engine)
        session = Session()
        checkExist = session.query()
