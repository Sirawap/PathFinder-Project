# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp_table_widget.ui',
# licensing of 'temp_table_widget.ui' applies.
#
# Created: Sat Jun  1 15:48:40 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 351, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 190, 221, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.combobox = QtWidgets.QComboBox(Form)
        self.combobox.setGeometry(QtCore.QRect(30, 260, 205, 18))
        self.combobox.setObjectName("combobox")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))
        self.combobox.setItemText(0, QtWidgets.QApplication.translate("Form", "  -- None --", None, -1))
        self.combobox.setItemText(1, QtWidgets.QApplication.translate("Form", "Alocohol", None, -1))
        self.combobox.setItemText(2, QtWidgets.QApplication.translate("Form", "Construction", None, -1))
        self.combobox.setItemText(3, QtWidgets.QApplication.translate("Form", "Domestic", None, -1))
        self.combobox.setItemText(4, QtWidgets.QApplication.translate("Form", "Financial instructor", None, -1))
        self.combobox.setItemText(5, QtWidgets.QApplication.translate("Form", "Health Service", None, -1))
        self.combobox.setItemText(6, QtWidgets.QApplication.translate("Form", "Manufacturer", None, -1))
        self.combobox.setItemText(7, QtWidgets.QApplication.translate("Form", "Mining", None, -1))
        self.combobox.setItemText(8, QtWidgets.QApplication.translate("Form", "Retail sales", None, -1))
        self.combobox.setItemText(9, QtWidgets.QApplication.translate("Form", "Service", None, -1))
        self.combobox.setItemText(10, QtWidgets.QApplication.translate("Form", "Transportation", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

