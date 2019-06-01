from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from src.accountClasses import UserAcc,CompanyAcc
from src.Jobseeker import Jobseeker
from src.Company import Company
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)

class LoginSystem():
    def __init__(self):
        pass

    def createCompany(self,usr,pwd,cname,email,tel):
        Session = sessionmaker(bind = engine)
        session = Session()
        ca = CompanyAcc(username = usr, password = pwd)
        c = Company(username = usr, companyName = cname,email=email,tel=tel,type = None)
        checkExist = session.query(CompanyAcc).filter(CompanyAcc.username == ca.username)
        boolExist = session.query(checkExist.exists()).scalar()
        checkCExist = session.query(Company).filter(Company.companyName == c.companyName)
        cboolExist = session.query(checkCExist.exists()).scalar()
        if boolExist or cboolExist :
            session.commit()
            session.close()
            return "Username or company name already exists"
        else:
            session.add(ca)
            session.add(c)
            session.commit()
            session.close()
            return "Done Register !"



    def createUser(self,usr,pwd,fname,surname,age,email,tel):
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
            user = Jobseeker(username = usr,fname= fname,surname = surname,email = email,age=age,tel=tel)
            session.add(user)
            session.add(ca)
            session.commit()
            session.close()
            return "Done Register !"


    def loginUser(self,user,pwd):
        Session = sessionmaker(bind=engine)
        session = Session()
        valid = False
        for row in session.query(UserAcc):
            if row.username == user and pwd == row.password:
                valid = True
        if valid:
            for row in session.query(Jobseeker).filter(Jobseeker.username == user):
                return Jobseeker(username = row.username,fname = row.fname,surname = row.surname,email= row.email,age = row.age,tel = row.tel)
        else:
            return "Username/Password incorrect"

    def loginCompany(self,user,pwd):
        Session = sessionmaker(bind=engine)
        session = Session()
        valid = False
        for row in session.query(CompanyAcc):
            if row.username == user and pwd == row.password:
                valid = True
        if valid:
            for row in session.query(Company).filter(Company.username == user):
                return Company(username= user,companyName = row.companyName,email = row.email, tel = row.tel)
        else:
            return "Username/Password incorrect"



