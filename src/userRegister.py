from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationships
from ui_py.User_Registeration_UI import Ui_register_user
from src.loginSystem import LoginSystem
class UserRegArea(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)


