# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_UI.ui',
# licensing of 'Login_UI.ui' applies.
#
# Created: Thu May  2 15:18:49 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(308, 262)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(80, 50, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(180, 50, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 110, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 81, 16))
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setGeometry(QtCore.QRect(140, 110, 131, 22))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(140, 140, 131, 22))
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Form", "Company", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Form", "User", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "User name :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Password  :", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "login", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

