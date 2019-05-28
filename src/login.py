from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationships
from ui_py.Login_UI import Ui_Form
from src.loginSystem import LoginSystem
class LoginArea(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.loginControl = LoginSystem()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.reg_b.clicked.connect(self.register)


    def reg(self):






