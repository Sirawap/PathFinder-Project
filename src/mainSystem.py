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

    def addUserEducation(self,user,field,degree,major,university):
        Session = sessionmaker(bind=engine)
        session = Session()

        checkExist = session.query(Education).filter(user.username == Education.username,field == Education.field,degree == Education.degree)
        boolExist = session.query(checkExist.exists()).scalar()
        if boolExist:
            session.commit()
            session.close()
            return "This Education already exists!"
        else:
            edu = Education(username = user.username,field = field,degree = degree,major = major,university=university)
            session.add(edu)
            session.commit()
            session.close()
            return
    def getAllEdu(self,user):

        Session = sessionmaker(bind=engine)
        session = Session()
        eduStr = ""
        eduLs = []
        for row in session.query(Education).filter(user.username == Education.username):
            eduStr = [str(row.field),str(row.degree),str(row.major),str(row.university)]
            eduLs.append(eduStr)

        session.commit()
        session.close()
        return eduLs

    def deleteEdu(self,user,field,degree):

        Session = sessionmaker(bind=engine)
        session = Session()
        deltarget = session.query(Education).filter(user.username == Education.username,field == Education.field,degree == Education.degree).first()

        session.delete(deltarget)
        session.commit()
        session.close()
        return

