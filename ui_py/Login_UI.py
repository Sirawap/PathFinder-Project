# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_UI.ui',
# licensing of 'Login_UI.ui' applies.
#
# Created: Sun Jun  2 12:51:32 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 373)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    color: rgb(255, 255, 255);\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QLabel#label_3{\n"
"    font: 16pt;\n"
"}\n"
"QLabel#error_label{\n"
"    color: red;\n"
"}\n"
"QRadioButton{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:white;\n"
"}\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 601, 353))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setStyleSheet("")
        self.username.setText("")
        self.username.setFrame(True)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet("")
        self.password.setText("")
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_2.addWidget(self.password)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.login_b = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.login_b.setStyleSheet("")
        self.login_b.setObjectName("login_b")
        self.horizontalLayout_4.addWidget(self.login_b)
        self.reg_b = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.reg_b.setObjectName("reg_b")
        self.horizontalLayout_4.addWidget(self.reg_b)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.error_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.error_label.setFont(font)
        self.error_label.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Login", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "User name :", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Password  :", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("Form", "Company", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("Form", "User", None, -1))
        self.login_b.setText(QtWidgets.QApplication.translate("Form", "login", None, -1))
        self.reg_b.setText(QtWidgets.QApplication.translate("Form", "Register", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

