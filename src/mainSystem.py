from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from src.accountClasses import UserAcc,CompanyAcc
from src.Jobseeker import Jobseeker
from src.Company import Company
from src.eduandjob import *
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)


class MainSystem():
    def __init__(self):
        pass

    def editUserProfile(self,user,fname,surname,age,tel,email):
        Session = sessionmaker(bind=engine)
        session = Session()

        edit = session.query(Jobseeker).filter(Jobseeker.username == user.username).first()

        edit.fname = fname
        edit.surname = surname
        edit.age = age
        edit.tel = tel
        edit.email = email

        session.commit()
        session.close()
