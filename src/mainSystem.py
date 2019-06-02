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

    def getCompanyAddress(self,com):

        Session = sessionmaker(bind=engine)
        session = Session()

        checkExist = session.query(Address).filter(com.companyName == Address.companyName)
        boolExist = session.query(checkExist.exists()).scalar()
        if boolExist:
            addrTarget = session.query(Address).filter(com.companyName == Address.companyName).first()
            session.commit()
            return Address(companyName = addrTarget.companyName, number = addrTarget.number,soi = addrTarget.soi,street = addrTarget.street,district = addrTarget.district,city = addrTarget.city,province = addrTarget.province,zipcode = addrTarget.zipcode)
        else:
            session.commit()
            session.close()
            return None

    def editCompanyProfile(self,com,tel,mail,type):
        Session = sessionmaker(bind=engine)
        session = Session()

        if type == "-- None --":
            type = None
        edit = session.query(Company).filter(Company.username == com.username,Company.companyName == com.companyName).first()

        edit.tel = tel
        edit.email = mail
        edit.type = type
        session.commit()
        session.close()
        return "Update Successfully"

    def editCompanyAddress(self,com,no,soi,street,district,city,province,zip):
        Session = sessionmaker(bind=engine)
        session = Session()
        edit = session.query(Address).filter_by(companyName = com.companyName).count()
        if edit == 0:
            adr = Address(companyName = com.companyName,no =no,soi =soi,street = street,district = district,city= city,province= province,zipcode = zip)
            session.add(adr)
            session.commit()
            session.close()
            return "Update Successfully"
        else:
            edit = session.query(Address).filter(Address.companyName == com.companyName).first()
            edit.no = no
            edit.soi = soi
            edit.street = street
            edit.district = district
            edit.city = city
            edit.province = province
            edit.zipcode = zip

            session.commit()
            session.close()
            return "Update Successfully"

    def addJob(self,com,jname,salary,sdesc,degree,field,exp,position):
        Session = sessionmaker(bind=engine)
        session = Session()
        count = session.query(Job).filter(Job.companyName == com.companyName, Job.jobName==jname).count()
        if count == 0:
            job = Job(companyName = com.companyName,jobName = jname,salary=salary,sdesc=sdesc,degree=degree,field=field,exp=exp,position=position)
            session.add(job)
            session.commit()
            session.close()
            return "New Job Posted Successfully"
        else :
            session.commit()
            session.close()
            return "Job Already Exists!"

    def getAllJob(self,com):

        Session = sessionmaker(bind=engine)
        session = Session()
        jobStr = ""
        jobLs = []
        for row in session.query(Job).filter(com.companyName == Job.companyName):
            jobStr = [str(row.jobName),str(row.position),str(row.salary),str(row.sdesc)]
            jobLs.append(jobStr)

        session.commit()
        session.close()
        return jobLs
    def deleteJob(self,com,jname):
        Session = sessionmaker(bind=engine)
        session = Session()

        delTarget = session.query(Job).filter(Job.companyName ==com.companyName,Job.jobName == jname).first()

        session.delete(delTarget)
        session.commit()
        session.close()
        return

    def getAllJobUser(self):

        Session = sessionmaker(bind=engine)
        session = Session()
        jobStr = ''
        jobLs = []

        for row in session.query(Job):
            jobStr = [str(row.companyName),str(row.field),str(row.jobName),str(row.position),str(row.salary),str(row.degree)]
            jobLs.append(jobStr)
        session.commit()
        session.close()

        return jobLs

    def getKeywordJobUser(self,compname,position,minSalary):
        Session = sessionmaker(bind=engine)
        session = Session()
        jobStr = ''
        jobLs = []
        if compname == "":
            if position == "":
                for row in session.query(Job).filter(Job.salary >= minSalary):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
            elif minSalary=="":
                for row in session.query(Job).filter(Job.position == position):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
            else:
                for row in session.query(Job).filter(Job.position == position,Job.salary >= minSalary):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
        elif position == "":
            if compname == "":
                for row in session.query(Job).filter(Job.salary >= minSalary):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
            elif minSalary=="":
                for row in session.query(Job).filter(Job.companyName == compname):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
            else:
                for row in session.query(Job).filter(Job.companyName == compname,Job.salary >= minSalary):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
        elif minSalary == "":
            if compname == "":
                for row in session.query(Job).filter(Job.position == position):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
            elif position=="":
                for row in session.query(Job).filter(Job.companyName == compname):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
            else:
                for row in session.query(Job).filter(Job.companyName == compname,Job.position == position):
                    jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                              str(row.salary), str(row.degree)]
                    jobLs.append(jobStr)
                return jobLs
        else:
            for row in session.query(Job).filter(Job.companyName == compname, Job.position == position,Job.salary >= minSalary):
                jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                          str(row.salary), str(row.degree)]
                jobLs.append(jobStr)
            return jobLs

    def getRecommendJobUser(self,user):
        Session = sessionmaker(bind=engine)
        session = Session()
        eduStr = ""
        eduLs = []
        jobStr = ''
        jobLs = []
        for row in session.query(Education).filter(user.username == Education.username):
            if str(row.field) in eduLs:
                continue
            eduStr = str(row.field)
            eduLs.append(eduStr)
        print(eduLs)
        for edu in eduLs:
            for row in session.query(Job).filter(Job.field == edu):
                jobStr = [str(row.companyName), str(row.field), str(row.jobName), str(row.position),
                          str(row.salary), str(row.degree)]
                jobLs.append(jobStr)
        print(jobLs)
        session.commit()
        session.close()
        return jobLs

    def getAllRequestUser(self,user):

        Session = sessionmaker(bind=engine)
        session = Session()
        reqStr = ''
        reqLs = []

        for row in session.query(Request).filter(Request.username == user.username):
            target = session.query(Jobseeker).filter(user.username == Jobseeker.username).first()
            name = target.fname
            reqStr = [str(row.companyName),str(row.fname),str(row.jobName),str(row.stat)]
            reqLs.append(reqStr)
        session.commit()
        session.close()

        return reqLs
    def getAllRequestCompany(self,com):

        Session = sessionmaker(bind=engine)
        session = Session()
        reqStr = ''
        reqLs = []

        for row in session.query(Request).filter(Request.companyName == com.companyName):
            target = session.query(Jobseeker).filter(row.username == Jobseeker.username).first()
            name = target.fname
            reqStr = [str(row.companyName),str(row.fname),str(row.username),str(row.jobName),str(row.stat)]
            reqLs.append(reqStr)
        session.commit()
        session.close()

        return reqLs

    def sendRequest(self,user,companyName,jobName):
        Session = sessionmaker(bind=engine)
        session = Session()

        checkExist = session.query(Request).filter(Request.companyName ==companyName,Request.jobName==jobName,Request.username == user.username)
        boolExist = session.query(checkExist.exists()).scalar()
        if boolExist:
            return "Request Already Exists!"
        else:
            req = Request(companyName = companyName,username = user.username,fname =user.fname,jobName = jobName, stat = "Pending")
            session.add(req)
            session.commit()
            session.close()
            return "Request Sent!"

    def acceptReq(self,com,fname,username,jobName):
        Session = sessionmaker(bind=engine)
        session = Session()

        edit =session.query(Request).filter(Request.companyName == com.companyName,Request.fname == fname,Request.username == username,Request.jobName == jobName).first()

        edit.stat = "Interest"

        session.commit()
        session.close()

    def declineReq(self, com, fname, username, jobName):
        Session = sessionmaker(bind=engine)
        session = Session()

        edit = session.query(Request).filter(Request.companyName == com.companyName, Request.fname == fname,
                                             Request.username == username, Request.jobName == jobName).first()

        edit.stat = "Not Interest"

        session.commit()
        session.close()

    def getJobDetail(self,com,jobName):
        Session = sessionmaker(bind=engine)
        session = Session()
        detail = ""

        for row in session.query(Job).filter(Job.companyName == com.companyName,Job.jobName == jobName):
            detail = [str(row.companyName),str(row.jobName),str(row.position),str(row.salary),str(row.sdesc),str(row.degree),str(row.field),str(row.exp)]

        return detail

    def getJobDetailUser(self,companyName,jobName):
        Session = sessionmaker(bind=engine)
        session = Session()
        detail = ""

        for row in session.query(Job).filter(Job.companyName == companyName, Job.jobName == jobName):
            detail = [str(row.companyName), str(row.jobName), str(row.position), str(row.salary), str(row.sdesc),
                      str(row.degree), str(row.field), str(row.exp)]

        return detail
    def reloadCompany(self,com):
        Session = sessionmaker(bind=engine)
        session = Session()

        target = session.query(Company).filter(Company.username == com.username).first()

        return Company(username = target.username,companyName = target.companyName,email = target.email,tel = target.tel,type = target.type)

    def reloadUser(self,user):
        Session = sessionmaker(bind=engine)
        session = Session()

        target = session.query(Jobseeker).filter(Jobseeker.username == user.username).first()

        return Jobseeker(username=target.username,fname=target.fname,surname=target.surname,email=target.email,age=target.age,tel=target.tel)

    def getUser(self,username):
        Session = sessionmaker(bind=engine)
        session = Session()

        target = session.query(Jobseeker).filter(Jobseeker.username == username).first()
        return Jobseeker(username=target.username, fname=target.fname, surname=target.surname, email=target.email,
                         age=target.age, tel=target.tel)
