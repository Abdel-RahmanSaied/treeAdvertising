from PyQt5 import QtWidgets , QtCore
from views import orderRequirment_view
import json
import os

class OrderRequirment(QtWidgets.QWidget, orderRequirment_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(OrderRequirment, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = OrderRequirment()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()