import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from src.login_GUI import Login_GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Login_GUI()
    w.show()

    sys.exit(app.exec_())