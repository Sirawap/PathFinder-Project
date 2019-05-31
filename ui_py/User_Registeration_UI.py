# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_Registeration_UI.ui',
# licensing of 'User_Registeration_UI.ui' applies.
#
# Created: Fri May 31 14:02:14 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_register_user(object):
    def setupUi(self, register_user):
        register_user.setObjectName("register_user")
        register_user.resize(469, 362)
        register_user.resize(469, 435)
        register_user.setStyleSheet("QWidget{\n"
"    background-color: black;\n"
"    color: white\n"
"}\n"
"\n"
"QComboBox{    \n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"\n"
"QLabel#error_label{    \n"
"    color: red;\n"
"}")
        self.confirm_b = QtWidgets.QPushButton(register_user)
        self.confirm_b.setGeometry(QtCore.QRect(180, 300, 93, 28))
        self.confirm_b.setObjectName("confirm_b")
        self.label = QtWidgets.QLabel(register_user)
        self.label.setGeometry(QtCore.QRect(30, 100, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(register_user)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(register_user)
        self.label_4.setGeometry(QtCore.QRect(180, 30, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(register_user)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(register_user)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(register_user)
        self.label_7.setGeometry(QtCore.QRect(310, 100, 53, 16))
        self.label_7.setObjectName("label_7")
        self.register_firstname = QtWidgets.QLineEdit(register_user)
        self.register_firstname.setGeometry(QtCore.QRect(110, 100, 161, 22))
        self.register_firstname.setObjectName("register_firstname")
        self.register_surname = QtWidgets.QLineEdit(register_user)
        self.register_surname.setGeometry(QtCore.QRect(110, 130, 161, 22))
        self.register_surname.setObjectName("register_surname")
        self.register_user_2 = QtWidgets.QLineEdit(register_user)
        self.register_user_2.setGeometry(QtCore.QRect(110, 200, 161, 22))
        self.register_user_2.setObjectName("register_user_2")
        self.register_password = QtWidgets.QLineEdit(register_user)
        self.register_password.setGeometry(QtCore.QRect(110, 230, 161, 22))
        self.register_password.setObjectName("register_password")
        self.register_age = QtWidgets.QLineEdit(register_user)
        self.register_age.setGeometry(QtCore.QRect(350, 100, 31, 22))
        self.register_age.setText("")
        self.register_age.setObjectName("register_age")
        self.register_rePassword = QtWidgets.QLineEdit(register_user)
        self.register_rePassword.setGeometry(QtCore.QRect(170, 260, 161, 22))
        self.register_rePassword.setObjectName("register_rePassword")
        self.label_15 = QtWidgets.QLabel(register_user)
        self.label_15.setGeometry(QtCore.QRect(30, 260, 141, 16))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(register_user)
        self.label_17.setGeometry(QtCore.QRect(280, 200, 16, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(register_user)
        self.label_18.setGeometry(QtCore.QRect(280, 230, 16, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(register_user)
        self.label_19.setGeometry(QtCore.QRect(340, 260, 16, 16))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(register_user)
        self.label_21.setGeometry(QtCore.QRect(280, 100, 16, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(register_user)
        self.label_22.setGeometry(QtCore.QRect(280, 130, 16, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(register_user)
        self.label_23.setGeometry(QtCore.QRect(30, 160, 61, 16))
        self.label_23.setObjectName("label_23")
        self.register_email = QtWidgets.QLineEdit(register_user)
        self.register_email.setGeometry(QtCore.QRect(110, 160, 161, 22))
        self.register_email.setObjectName("register_email")
        self.label_24 = QtWidgets.QLabel(register_user)
        self.label_24.setGeometry(QtCore.QRect(290, 160, 31, 16))
        self.label_24.setObjectName("label_24")
        self.register_tel = QtWidgets.QLineEdit(register_user)
        self.register_tel.setGeometry(QtCore.QRect(330, 160, 91, 22))
        self.register_tel.setText("")
        self.register_tel.setObjectName("register_tel")
        self.error_label = QtWidgets.QLabel(register_user)
        self.error_label.setGeometry(QtCore.QRect(50, 350, 351, 51))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")

        self.retranslateUi(register_user)
        QtCore.QMetaObject.connectSlotsByName(register_user)

    def retranslateUi(self, register_user):
        register_user.setWindowTitle(QtWidgets.QApplication.translate("register_user", "Form", None, -1))
        self.confirm_b.setText(QtWidgets.QApplication.translate("register_user", "Confirm", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("register_user", "First name:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("register_user", "Surname  :", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("register_user", "Register", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("register_user", "User name :", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("register_user", "Password   :", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("register_user", "Age :", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("register_user", "Re-confirm Password  :", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("register_user", "*", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("register_user", "*", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("register_user", "*", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("register_user", "*", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("register_user", "*", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("register_user", "email :", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("register_user", "Tel :", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    register_user = QtWidgets.QWidget()
    ui = Ui_register_user()
    ui.setupUi(register_user)
    register_user.show()
    sys.exit(app.exec_())

