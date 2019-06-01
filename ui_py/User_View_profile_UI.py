# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_View_profile_UI.ui',
# licensing of 'User_View_profile_UI.ui' applies.
#
# Created: Sat Jun  1 13:10:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 491)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_Firstname = QtWidgets.QLabel(Form)
        self.label_Firstname.setGeometry(QtCore.QRect(110, 100, 151, 24))
        self.label_Firstname.setObjectName("label_Firstname")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 51, 24))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 57, 24))
        self.label_3.setObjectName("label_3")
        self.label_Surname = QtWidgets.QLabel(Form)
        self.label_Surname.setGeometry(QtCore.QRect(110, 120, 151, 21))
        self.label_Surname.setObjectName("label_Surname")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(320, 100, 41, 24))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(320, 120, 23, 24))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 140, 27, 24))
        self.label_4.setObjectName("label_4")
        self.label_mail = QtWidgets.QLabel(Form)
        self.label_mail.setGeometry(QtCore.QRect(370, 100, 201, 24))
        self.label_mail.setObjectName("label_mail")
        self.label_tel = QtWidgets.QLabel(Form)
        self.label_tel.setGeometry(QtCore.QRect(380, 120, 101, 24))
        self.label_tel.setObjectName("label_tel")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(70, 140, 31, 24))
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(320, 140, 41, 24))
        self.label_15.setObjectName("label_15")
        self.label_home = QtWidgets.QLabel(Form)
        self.label_home.setGeometry(QtCore.QRect(380, 140, 91, 21))
        self.label_home.setObjectName("label_home")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(40, 350, 271, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(40, 170, 211, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.frame_experience = QtWidgets.QFrame(Form)
        self.frame_experience.setGeometry(QtCore.QRect(40, 380, 460, 71))
        self.frame_experience.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_experience.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_experience.setObjectName("frame_experience")
        self.tableWidget_educatio_background = QtWidgets.QTableWidget(Form)
        self.tableWidget_educatio_background.setGeometry(QtCore.QRect(40, 210, 460, 121))
        self.tableWidget_educatio_background.setObjectName("tableWidget_educatio_background")
        self.tableWidget_educatio_background.setColumnCount(0)
        self.tableWidget_educatio_background.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "USER Profile", None, -1))
        self.label_Firstname.setText(QtWidgets.QApplication.translate("Form", "Pawaris", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Name:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Surname:", None, -1))
        self.label_Surname.setText(QtWidgets.QApplication.translate("Form", "Lertchaiprasert", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "E-mail:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Tel:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Age:", None, -1))
        self.label_mail.setText(QtWidgets.QApplication.translate("Form", "60090027@kmitl.ac.th", None, -1))
        self.label_tel.setText(QtWidgets.QApplication.translate("Form", "061-842-8222", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "19", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Form", "Home :", None, -1))
        self.label_home.setText(QtWidgets.QApplication.translate("Form", "02 -3291790", None, -1))
        self.label_27.setText(QtWidgets.QApplication.translate("Form", "Working expereince/Projects", None, -1))
        self.label_28.setText(QtWidgets.QApplication.translate("Form", "Education Background", None, -1))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

