from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from views import main_view



class Main_manger(QtWidgets.QWidget, main_view.Ui_main):

    def __init__(self , name=None, *args, **kwargs ):
        super(Main_manger, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Main_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()