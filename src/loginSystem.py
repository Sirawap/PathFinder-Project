from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from src.accountClasses import UserAcc,CompanyAcc
from src.Jobseeker import Jobseeker
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)

class LoginSystem():
    def __init__(self):
        pass

    def createCompany(self,usr,pwd):
        Session = sessionmaker(bind = engine)
        session = Session()
        ca = CompanyAcc(username = usr, password = pwd)
        checkExist = session.query(CompanyAcc).filter(CompanyAcc.username == ca.username)
        boolExist = session.query(checkExist.exists()).scalar()
        if boolExist:
            session.commit()
            session.close()
            return "Username for Company already exists"
        else:
            session.add(ca)
            session.commit()
            session.close()
            return "Done Register !"



    def createUser(self,usr,pwd,fname,surname,age,email,tel,major,lang):
        Session = sessionmaker(bind = engine)
        session = Session()
        ca = UserAcc(username = usr, password = pwd)
        checkExist = session.query(UserAcc).filter(UserAcc.username == ca.username)
        boolExist = session.query(checkExist.exists()).scalar()
        if boolExist:
            session.commit()
            session.close()
            return "Username for User already exists"
        else:
            user = Jobseeker(username = usr,fname= fname,surname = surname,email = email,major=major,lang=lang,age=age,tel=tel)
            session.add(user)
            session.add(ca)
            session.commit()
            session.close()
            return "Done Register !"



