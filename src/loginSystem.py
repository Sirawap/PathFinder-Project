from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from src.accountClasses import UserAcc,CompanyAcc

engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)

class LoginSystem():
    def __init__(self):
        pass

    def createCompany(self,usr,pwd):
        Session = sessionmaker(bind = self.engine)
        session = Session()
        ca = CompanyAcc(username = usr, password = pwd)
        checkExist = session.query(CompanyAcc).filter(CompanyAcc.username == ca.username)
        boolExist = session.query(checkExist.exists()).scalar()
        if boolExist:
            return "Username for Company already exists"
        else:
            session.add(ca)
            return "Done Register !"

        session.commit()
        session.close()

    def createUser(self,usr,pwd):
        Session = sessionmaker(bind = self.engine)
        session = Session()
        ca = UserAcc(username = usr, password = pwd)
        checkExist = session.query(CompanyAcc).filter(CompanyAcc.username == ca.username)
        boolExist = session.query(checkExist.exists()).scalar()
        if boolExist:
            session.commit()
            session.close()
            return "Username for User already exists"
        else:
            session.add(ca)
            session.commit()
            session.close()
            return "Done Register !"



