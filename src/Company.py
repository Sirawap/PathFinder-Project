from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
base = declarative_base()
engine = create_engine("mysql+pymysql://root:pathfinder@127.0.0.1:3307/pathfinderDB",echo = True)

class Company(base):
    # __tablename__ = "company"
    #
    # username = Column("username",primary_key=True)
    # companyName= Column("companyName",unique=True)
    # email = Column("email",unique=True)
    # tel = Column("tel",unique=True)
    # type = Column("type",unique=False)

    def __init__(self):
        __tablename__ = "company"

        self.username = Column("username",primary_key=True)
        self.companyName= Column("companyName",unique=True)
        self.email = Column("email",unique=True)
        self.tel = Column("tel",unique=True)
        self.type = Column("type",unique=False)

    def getUsername(self):
        return self.username

    def getCompanyName(self):
        return self.companyName

    def getEmail(self):
        return self.email

    def getTel(self):
        return self.tel


    def getAddNo(self):
        pass

    def getAddSoi(self):
        pass

    def getAddSt(self):
        pass

    def getAddDistrict(self):
        pass

    def getAddCity(self):
        pass

    def getAddProvince(self):
        pass

    def getAddZip(self):
        pass

    def getType(self):
        return self.type
