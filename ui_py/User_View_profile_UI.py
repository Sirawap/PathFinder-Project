# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User_View_profile_UI.ui',
# licensing of 'User_View_profile_UI.ui' applies.
#
# Created: Wed May 29 11:32:33 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 538)
        Form.setStyleSheet("QWidget{\n"
"    background-image: url(:/bg/grey.png);\n"
"    color: white\n"
"}\n"
"\n"
"url(:/bg/grey.png)")
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
        self.label_address = QtWidgets.QLabel(Form)
        self.label_address.setGeometry(QtCore.QRect(120, 170, 381, 21))
        self.label_address.setObjectName("label_address")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(40, 170, 61, 24))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(320, 140, 41, 24))
        self.label_15.setObjectName("label_15")
        self.label_home = QtWidgets.QLabel(Form)
        self.label_home.setGeometry(QtCore.QRect(380, 140, 91, 21))
        self.label_home.setObjectName("label_home")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(200, 140, 51, 24))
        self.label_13.setObjectName("label_13")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(140, 140, 51, 24))
        self.label_17.setObjectName("label_17")
        self.frame_education = QtWidgets.QFrame(Form)
        self.frame_education.setGeometry(QtCore.QRect(40, 240, 471, 91))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.frame_education.setFont(font)
        self.frame_education.setAutoFillBackground(False)
        self.frame_education.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_education.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_education.setObjectName("frame_education")
        self.label_23 = QtWidgets.QLabel(self.frame_education)
        self.label_23.setGeometry(QtCore.QRect(70, 20, 151, 24))
        self.label_23.setObjectName("label_23")
        self.label_21 = QtWidgets.QLabel(self.frame_education)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 50, 24))
        self.label_21.setObjectName("label_21")
        self.label_18 = QtWidgets.QLabel(self.frame_education)
        self.label_18.setGeometry(QtCore.QRect(280, 0, 57, 24))
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.frame_education)
        self.label_22.setGeometry(QtCore.QRect(330, 0, 111, 24))
        self.label_22.setObjectName("label_22")
        self.label_20 = QtWidgets.QLabel(self.frame_education)
        self.label_20.setGeometry(QtCore.QRect(0, 20, 61, 21))
        self.label_20.setObjectName("label_20")
        self.label_19 = QtWidgets.QLabel(self.frame_education)
        self.label_19.setGeometry(QtCore.QRect(50, 0, 211, 24))
        self.label_19.setObjectName("label_19")
        self.label_24 = QtWidgets.QLabel(self.frame_education)
        self.label_24.setGeometry(QtCore.QRect(0, 40, 50, 24))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_education)
        self.label_25.setGeometry(QtCore.QRect(0, 60, 61, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_education)
        self.label_26.setGeometry(QtCore.QRect(280, 40, 57, 24))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(40, 350, 271, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(40, 210, 211, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.frame_experience = QtWidgets.QFrame(Form)
        self.frame_experience.setGeometry(QtCore.QRect(40, 380, 471, 71))
        self.frame_experience.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_experience.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_experience.setObjectName("frame_experience")

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
        self.label_address.setText(QtWidgets.QApplication.translate("Form", "NO. - Street - District - Provience - City - Zipcode", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Address  :", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Form", "Home :", None, -1))
        self.label_home.setText(QtWidgets.QApplication.translate("Form", "02 -3291790", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Form", "Male", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "Gender :", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("Form", "KMITL", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("Form", "Major:", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Form", "Degree:", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("Form", "Bachelor Degree", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("Form", "University:", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("Form", "Software Engineering", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("Form", "Major:", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("Form", "University:", None, -1))
        self.label_26.setText(QtWidgets.QApplication.translate("Form", "Degree:", None, -1))
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
