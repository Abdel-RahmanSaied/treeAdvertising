from PyQt5 import QtWidgets , QtCore
from views import newOrder_view
import json
import requests
import os

class NewOrderView_manger(QtWidgets.QWidget, newOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(NewOrderView_manger, self).__init__()
        self.setupUi(self)

        self.clientDesign_btn.clicked.connect(self.getdesign_path)
        self.upload_photo_btn.clicked.connect(self.getphoto_path)
        self.search_btn.clicked.connect(self.check_client)

        self.client_check_url = 'https://saied.pythonanywhere.com/clientPhone/'
        self.add_client_url = 'https://saied.pythonanywhere.com/clients/'

        self.token = 'a3f482dc51cf4cf3d3ecbe8e469c8048c09c333a'
        self.headers = {}

        '''
        data
        '''
        self.username = ''
        self.level = ''
        self.recived_date = ''
        self.post_date = ''
        self.phone_number = ''



    def getdesign_path(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'تحديد مسار الملف ', '', 'Images (*.png, *.jpeg , *.jpg , *.psd , *.ai , *.eps ) ')
        if len(self.fileName) != 0 :
            self.filaPath_lbl.setText(self.fileName)
            #self.checkAcceptedSignal.emit()
        else :
            self.filaPath_lbl.setText('مسار الملف ')
    def getphoto_path(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'تحديد مسار الملف ', '', 'Images (*.png, *.jpeg , *.jpg , *.psd , *.ai , *.eps ) ')
        if len(self.fileName) != 0 :
            self.filaPath_lbl_2.setText(self.fileName)
            #self.checkAcceptedSignal.emit()
        else :
            self.filaPath_lbl_2.setText('مسار الملف ')

    def check_client(self):
        msg = QtWidgets.QMessageBox()
        self.headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        self.username = self.username_lin_3.text()
        try :
            if self.redRadioButton.isChecked():
                self.level = "R"
            elif self.blueRadioButton.isChecked():
                self.level = "B"
            elif self.greenRadioButton.isChecked():
                self.level = "G"
        except Exception as r :
            print(r)

        self.recived_date = self.recived_date_lin.text()
        self.post_date = self.post_date_lin.text()
        self.phone_number = self.phone_number_lin.text()

        phone_number = {
                "phone": self.phone_number
                            }

        client_data = {
                "name": self.username,
                "phone_number": self.phone_number,
                "clientlevel": self.level
            }
        if self.phone_number == '':
            msg.setWindowTitle("Alarm")
            msg.setText("please enter phone number ")
            msg.exec_()
        else:
            try :
                check_reply = requests.post(self.client_check_url, json = phone_number, headers=self.headers).json()
            except Exception as s :
                print("ss",s)

            try :
                if check_reply['Response'] == "client does not exist":
                        #add_user_reply = requests.post(self.add_client_url, json=client_data, headers=self.headers).json()
                        msg.setWindowTitle("Alarm")
                        msg.setText("client does not exist please enter all data")
                        msg.exec_()
                        #print(add_user_reply)
                elif check_reply['Response'] == "successful":
                    self.username_lin_3.setText(check_reply['name'])
                    print(check_reply)
                    if check_reply['clientlevel'] == 'R' :
                        self.redRadioButton.setChecked(True)
                    elif check_reply['clientlevel'] == 'B' :
                        self.blueRadioButton.setChecked(True)
                    elif check_reply['clientlevel'] == 'G' :
                        self.greenRadioButton.setChecked(True)
                    msg.setWindowTitle("Alarm")
                    msg.setText("client data imported successfully")
                    msg.exec_()

            except Exception as e :
                print(e)

    def add_new_order(self):
        pass

if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = NewOrderView_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()