from PyQt5 import QtWidgets , QtCore
from views import followOrder_view
import json
import os

class FollowOrder(QtWidgets.QWidget, followOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(FollowOrder, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = FollowOrder()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()