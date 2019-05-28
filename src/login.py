from PySide2 import QtWidgets,QtCore,QtGui
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationships
from ui_py.Login_UI import Ui_Form

