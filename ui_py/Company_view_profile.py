# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company_view_profile.ui',
# licensing of 'Company_view_profile.ui' applies.
#
# Created: Sun Jun  2 11:39:38 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 391)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 20, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(40, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 210, 441, 73))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_5.addWidget(self.label_13)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_5.addWidget(self.label_21)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_6.addWidget(self.label_22)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_7.addWidget(self.label_23)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 110, 441, 47))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.label_comp_type = QtWidgets.QLabel(self.layoutWidget1)
        self.label_comp_type.setObjectName("label_comp_type")
        self.horizontalLayout_12.addWidget(self.label_comp_type)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_12)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_11.addWidget(self.label_4)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "COMPANY Profile", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Form", "Address", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Form", "No.", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Form", "Soi:", None, -1))
        self.label_18.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("Form", "Street:", None, -1))
        self.label_19.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("Form", "District/Tambon:", None, -1))
        self.label_20.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Form", "City/Ampur:", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("Form", "Province/State:", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate("Form", " Zip Code:", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Company name:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "Company Type", None, -1))
        self.label_comp_type.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Tel :", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Email :", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Form", "Null", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

