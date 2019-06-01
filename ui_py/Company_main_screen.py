# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company_main_screen.ui',
# licensing of 'Company_main_screen.ui' applies.
#
# Created: Sat Jun  1 12:58:04 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: rgb(60,60,60);\n"
"    font: \"Arial\";\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 120, 691, 401))
        self.tableWidget.setStyleSheet("color: black;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.setColumnWidth(3,400)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuJob_Negitiate = QtWidgets.QMenu(self.menubar)
        self.menuJob_Negitiate.setObjectName("menuJob_Negitiate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLog_Out = QtWidgets.QAction(MainWindow)
        self.actionLog_Out.setObjectName("actionLog_Out")
        self.actionEdit_Profile = QtWidgets.QAction(MainWindow)
        self.actionEdit_Profile.setObjectName("actionEdit_Profile")
        self.actionView_Profile = QtWidgets.QAction(MainWindow)
        self.actionView_Profile.setObjectName("actionView_Profile")
        self.actionPost_Job = QtWidgets.QAction(MainWindow)
        self.actionPost_Job.setObjectName("actionPost_Job")
        self.actionView_Recived_Job_Offer = QtWidgets.QAction(MainWindow)
        self.actionView_Recived_Job_Offer.setObjectName("actionView_Recived_Job_Offer")
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionLog_Out)
        self.menuMain.addSeparator()
        self.menuMain.addAction(self.actionEdit_Profile)
        self.menuMain.addAction(self.actionView_Profile)
        self.menuMain.addSeparator()
        self.menuJob_Negitiate.addAction(self.actionPost_Job)
        self.menuJob_Negitiate.addAction(self.actionView_Recived_Job_Offer)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuJob_Negitiate.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "All Posted Job Offer", None, -1))
        self.tableWidget.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Job name", None, -1))
        self.tableWidget.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Position", None, -1))
        self.tableWidget.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Salary", None, -1))
        self.tableWidget.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "description", None, -1))
        self.menuMain.setTitle(QtWidgets.QApplication.translate("MainWindow", "Main", None, -1))
        self.menuJob_Negitiate.setTitle(QtWidgets.QApplication.translate("MainWindow", "Job Negitiate", None, -1))
        self.actionLog_Out.setText(QtWidgets.QApplication.translate("MainWindow", "Log Out", None, -1))
        self.actionEdit_Profile.setText(QtWidgets.QApplication.translate("MainWindow", "Edit Profile", None, -1))
        self.actionView_Profile.setText(QtWidgets.QApplication.translate("MainWindow", "View Profile", None, -1))
        self.actionPost_Job.setText(QtWidgets.QApplication.translate("MainWindow", "Post Job", None, -1))
        self.actionView_Recived_Job_Offer.setText(QtWidgets.QApplication.translate("MainWindow", "View Recived Job Offer", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

