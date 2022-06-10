from PyQt5 import QtWidgets , QtCore
from views import add_client_view
from PyQt5.QtWidgets import *
import json
import requests
import os

class AddClients(QtWidgets.QWidget, add_client_view.Ui_Form):
    checkDataSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(AddClients, self).__init__()
        self.setupUi(self)

        self.base_url = "https://saied.pythonanywhere.com/clients/"
        self.token = ''
        self.add_btn.clicked.connect(self.run)

    def run(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}

        msg = QtWidgets.QMessageBox()
        name = self.name_lin.text()
        phone = self.phone_lin.text()
        level = ''
        if self.redRadioButton.isChecked():
            level = "R"
        elif self.blueRadioButton.isChecked():
            level = "B"
        elif self.greenRadioButton.isChecked():
            level = "G"
        else:
            level = ''
        notes = self.textEdit.toPlainText()

        if len(name) == 0 :
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        elif len(phone) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        elif level == '':
            msg.setWindowTitle("Warning")
            msg.setText("you must set level color !")
            msg.exec_()
        else:
            if len(notes) != 0 :
                data = {
                        "name": name,
                        "phone_number": phone,
                        "notes": notes,
                        "clientlevel": level
                        }
            else:
                data = {
                    "name": name,
                    "phone_number": phone,
                    "clientlevel": level
                }

            try:
                self.add_client = requests.post(self.base_url, json=data, headers=headers)
                self.checkDataSignal.emit()
                if self.add_client.status_code == 406:
                    msg.setWindowTitle("Warning")
                    msg.setText(self.add_client.json()['Response'])
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
    w = AddClients()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()