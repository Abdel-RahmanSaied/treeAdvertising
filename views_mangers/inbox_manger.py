from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from views import inbox_view

class Inbox_manger(QtWidgets.QWidget, inbox_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    logout_signal = QtCore.pyqtSignal()
    def __init__(self , name=None, *args, **kwargs ):
        super(Inbox_manger, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Inbox_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()