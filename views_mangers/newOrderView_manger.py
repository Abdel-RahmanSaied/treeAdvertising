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
        self.save_btn.clicked.connect(self.add_new_order)

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

        self.design_types = ''
        self.img_path = ''
        self.design_path = ''
        self.design_category = []
        self.printing_type = []
        self.size_width = 0.0
        self.size_high = 0.0
        self.materials = ''
        self.color = ''
        self.thickness = 0.0
        self.Post_print_services = []
        self.state = ''
        self.notes = ''
        self.cliend_id = 0

    def getdesign_path(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'تحديد مسار الملف ', '', 'Images (*.png, *.jpeg , *.jpg , *.psd , *.ai , *.eps ) ')
        if len(self.fileName) != 0 :
            self.filaPath_lbl.setText(self.fileName)
            #self.checkAcceptedSignal.emit()
        else :
            self.filaPath_lbl.setText('مسار الملف')
    def getphoto_path(self):
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'تحديد مسار الملف ', '', 'Images (*.png, *.jpeg , *.jpg , *.psd , *.ai , *.eps ) ')
        if len(self.fileName) != 0 :
            self.filaPath_lbl_2.setText(self.fileName)
            #self.checkAcceptedSignal.emit()
        else :
            self.filaPath_lbl_2.setText('مسار الملف')

    def check_client(self):
        msg = QtWidgets.QMessageBox()
        self.headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}
        self.username = self.username_lin_3.text()
        try:
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
                    if check_reply['clientlevel'] == 'R':
                        self.redRadioButton.setChecked(True)
                    elif check_reply['clientlevel'] == 'B' :
                        self.blueRadioButton.setChecked(True)
                    elif check_reply['clientlevel'] == 'G' :
                        self.greenRadioButton.setChecked(True)
                    self.cliend_id = check_reply['id']
                    msg.setWindowTitle("Alarm")
                    msg.setText("client data imported successfully")
                    msg.exec_()

            except Exception as e :
                print(e)

    def add_new_order(self):
        try:
            msg = QtWidgets.QMessageBox()
            if self.ofice_design.isChecked() :
                self.design_types= "O"
            elif self.attatched_design.isChecked():
                self.design_types = 'A'

            if self.filaPath_lbl.text() != 'مسار الملف' :
                self.design_path = self.filaPath_lbl.text()
            else :
                self.design_path = 'no file selected '

            if self.filaPath_lbl_2.text() != 'مسار الملف':
                self.img_path = self.filaPath_lbl_2.text()
            else :
                self.img_path = 'no file selected '

            if self.logo_checkBox.isChecked() :
                self.design_category.append("logo")

            if self.businessCard_checkBox.isChecked() :
                self.design_category.append("business Card")

            if self.banner_checkBox.isChecked():
                self.design_category.append("banner")

            if self.brochure_checkBox.isChecked():
                self.design_category.append("brochure")

            if self.menu_checkBox.isChecked():
                self.design_category.append("menu")

            if self.flyer_checkBox.isChecked():
                self.design_category.append("flyer")

            if self.certificate_checkBox.isChecked():
                self.design_category.append("certificate")

            if self.cover_checkBox.isChecked():
                self.design_category.append("cover")

            if self.poster_checkBox.isChecked():
                self.design_category.append("poster")

            if self.rollUp_checkBox.isChecked():
                self.design_category.append("RollUp")

            if self.label_checkBox.isChecked():
                self.design_category.append("label")

            if len(self.other_lineEdit.text()) != 0 :
                self.design_category.append(self.other_lineEdit.text())

            if self.digital_checkBox.isChecked():
                self.printing_type.append("ديجيتال")

            if self.offset_checkBox.isChecked():
                self.printing_type.append("اوفسيت")

            if self.silkscreen_checkBox.isChecked():
                self.printing_type.append("سلك سكرين")

            if self.uv_checkBox.isChecked():
                self.printing_type.append("UV")

            if self.indoor_checkBox.isChecked():
                self.printing_type.append("ان دور")

            if self.outdoor_checkBox.isChecked():
                self.printing_type.append("اوت دور")

            if self.flexo_checkBox.isChecked():
                self.printing_type.append("فلكسو")

            if self.laser_checkBox.isChecked():
                self.printing_type.append("ليزر")

            if self.fiber_checkBox.isChecked():
                self.printing_type.append("فايبر")

            if self.selmation_checkBox.isChecked():
                self.printing_type.append("سيلميشن")

            if self.Cutter_checkBox.isChecked():
                self.printing_type.append("كتر بلوتر")

            if self.inkjet_checkBox.isChecked():
                self.printing_type.append("انك جيت")

            self.size_high = float(self.high_doubleSpinBox.text())
            self.size_width = float(self.width_doubleSpinBox.text())



            """ Check Input Data """
            if self.design_types == '':
                msg.setWindowTitle("Warning")
                msg.setText("You must choose design type !")
                msg.exec_()
                self.design_category = []
                self.printing_type = []


            """ Depug """
            print(40*"-")
            print("img_path : ",self.img_path)
            print("design_path : ",self.design_path)
            print("design_types : ",self.design_types)
            print("design_category : ",self.design_category)
            print("printing_type : ",self.printing_type)
            print("size_high : ",self.size_high)
            print("size_width : ",self.size_width)


            print(self.design_category)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = NewOrderView_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()