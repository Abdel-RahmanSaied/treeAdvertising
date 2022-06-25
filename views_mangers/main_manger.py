from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from views import main_view
import json
import os
import time
import datetime
from threading import Timer


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)
    time_signal = pyqtSignal()

    def __init__(self, widget ):
        super().__init__(widget)
        self._widget = widget

        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)
    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)

class Main_manger(QtWidgets.QWidget, main_view.Ui_main):
    checkAcceptedSignal = QtCore.pyqtSignal()
    logout_signal = QtCore.pyqtSignal()
    def __init__(self , name=None, *args, **kwargs ):
        super(Main_manger, self).__init__()
        self.setupUi(self)
        # self.setMouseTracking(True)
        try :
            self.thred = RepeatTimer(1, self.start_time)

        except Exception as w :
            print(w)
        try :
            tracker = MouseTracker(self)
            tracker.positionChanged.connect(self.on_positionChanged)
        except Exception as e :
            print(e)

        self.begin_timer = 0
        self.session_counter = 0


    def start_stopwatch(self):
        try :
            self.thred.start()
            self.begin_timer = time.time()
            self.session_counter = time.time()
        except Exception as e:
            print(e)

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChanged(self, pos):

        self.session_counter = time.time()
        #print("(%d, %d)" % (pos.x(), pos.y()))

    def start_time(self):
        end_time = time.time()
        lapced_time = end_time - self.begin_timer
        mins = lapced_time // 60
        sec = round(lapced_time % 60)
        hours = mins // 60
        mins = mins % 60
        session_time = str("{0}:{1}:{2}".format(int(hours), int(mins), sec))
        self.sessionTime_lbl.setText(session_time)
        end_time_session = time.time()
        actuall_session_time = end_time_session - self.session_counter
        session_mins = actuall_session_time // 60
        session_mins = session_mins % 60
        if session_mins == 1 :
            #self.logout_signal.emit()
            pass



if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Main_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()