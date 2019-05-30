# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Company_main_screen.ui',
# licensing of 'Company_main_screen.ui' applies.
#
# Created: Thu May 30 11:56:50 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 80, 331, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "gu kid mai out  for the posted job history list", None, -1))
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

