import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import ui_py.Company_main_screen
import src.login_GUI
import src.Company_Profile_GUI
import src.EditComp_Profile_GUI

class Comp_Main_GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self,None)

        self.comp_ui = ui_py.Company_main_screen.Ui_MainWindow()
        self.comp_ui.setupUi(self)

        self.comp_ui.actionLog_Out.triggered.connect(self.logOut)
        self.comp_ui.actionEdit_Profile.triggered.connect(self.openEditProfile)
        self.comp_ui.actionView_Profile.triggered.connect(self.openViewProfile)


    def logOut(self):
        self.login_ui = src.login_GUI.Login_GUI()
        self.login_ui.show()
        self.close()

    def openEditProfile(self):
        self.compE_P_ui = src.EditComp_Profile_GUI.Edit_Company_Profile_GUI()
        self.compE_P_ui.show()

    def openViewProfile(self):
        self.compV_P_ui = src.Company_Profile_GUI.Edit_Company_Profile_GUI()
        self.compV_P_ui.show()

    def openPostedJob(self):
        pass

    def openRecivedJobOffer(self):
        pass
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv);
#     w = Comp_Main_GUI()
#     w.show()
#
#     sys.exit(app.exec_())
