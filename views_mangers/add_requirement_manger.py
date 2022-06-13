from PyQt5 import QtWidgets , QtCore
from views import add_requirement_view
from PyQt5.QtWidgets import *
import json
import requests
import os

class AddRequirement(QtWidgets.QWidget, add_requirement_view.Ui_Form):
    checkDataSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(AddRequirement, self).__init__()
        self.setupUi(self)

        self.base_url = "https://saied.pythonanywhere.com/requirements/"
        self.token = ''
        self.add_btn.clicked.connect(self.run)

    def run(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}

        msg = QtWidgets.QMessageBox()
        name = self.name_lin.text()
        quantity = self.spinBox.text()

        if len(name) == 0 :
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        else:

            data = {
                "product_name":name,
                "quantity":quantity,
                "acceptable_by": "not accepted"
                }

            try:
                self.post_reply = requests.post(self.base_url, json=data, headers=headers)
                self.checkDataSignal.emit()
                if self.post_reply.status_code == 406:
                    msg.setWindowTitle("Warning")
                    msg.setText(self.post_reply.json()['Response'])
                    msg.exec_()
            except (requests.ConnectionError, requests.Timeout) as exception:
                print(exception)
                msg.setWindowTitle("Warning")
                msg.setText("No internet connection.")
                msg.exec_()
            except Exception as e:
                print(e)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = AddRequirement()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()