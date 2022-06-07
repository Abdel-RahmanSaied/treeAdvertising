from PyQt5 import QtWidgets , QtCore
from views import followOrder_view
import json
import requests
import os

class FollowOrder(QtWidgets.QWidget, followOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(FollowOrder, self).__init__()
        self.setupUi(self)

        self.base_url = "https://saied.pythonanywhere.com/orders/"
        self.token = ''
    def run(self):
        msg = QtWidgets.QMessageBox()

        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        try :
            self.reply = requests.get(self.base_url , headers=headers).json()
            print(self.reply)
        except Exception as s :
            print("ss",s)
        try :
            self.listWidget.clear()

            for element in  self.reply :
                self.listWidget.addItem(str(element['order_id']))

        except Exception as e :
            print(e)





if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = FollowOrder()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()