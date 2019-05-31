# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_UI.ui',
# licensing of 'Login_UI.ui' applies.
#
# Created: Fri May 31 16:08:31 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 243)
        Form.setStyleSheet("QWidget{\n"
"    \n"
"    background-image: url(:/bg/grey.png);\n"
"    font: url(:/bg/grey.png)\"Arial\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: white;\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLabel#label_3{\n"
"    font: 16pt;\n"
"}\n"
"\n"
"QRadioButton{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white;\n"
"}\n"
"")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(70, 150, 95, 20))
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 150, 95, 20))
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 80, 81, 16))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 81, 16))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(140, 80, 131, 22))
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setStyleSheet("")
        self.username.setFrame(True)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(140, 110, 131, 22))
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet("")
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login_b = QtWidgets.QPushButton(Form)
        self.login_b.setGeometry(QtCore.QRect(50, 190, 93, 28))
        self.login_b.setStyleSheet("")
        self.login_b.setObjectName("login_b")
        self.reg_b = QtWidgets.QPushButton(Form)
        self.reg_b.setGeometry(QtCore.QRect(160, 190, 93, 28))
        self.reg_b.setObjectName("reg_b")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Form", "Company", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Form", "User", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "User name :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Password  :", None, -1))
        self.username.setText(QtWidgets.QApplication.translate("Form", "asdf", None, -1))
        self.password.setText(QtWidgets.QApplication.translate("Form", "asdf", None, -1))
        self.login_b.setText(QtWidgets.QApplication.translate("Form", "login", None, -1))
        self.reg_b.setText(QtWidgets.QApplication.translate("Form", "Register", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Login", None, -1))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

