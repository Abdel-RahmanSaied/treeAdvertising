from PyQt5 import QtWidgets , QtCore
from views import notes_view
import json
import os

class NotesManger(QtWidgets.QWidget, notes_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(NotesManger, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = NotesManger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()