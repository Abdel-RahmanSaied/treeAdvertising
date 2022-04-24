from PyQt5 import QtWidgets , QtCore
from views import newOrder_view
import json
import os

class NewOrderView_manger(QtWidgets.QWidget, newOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(NewOrderView_manger, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = NewOrderView_manger()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()