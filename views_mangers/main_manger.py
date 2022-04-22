from PyQt5 import QtWidgets , QtCore
from views import main_view
import json
import os

class Main_manger(QtWidgets.QWidget, main_view.Ui_main):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Main_manger, self).__init__()
        self.setupUi(self)




if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = Main_manger()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()