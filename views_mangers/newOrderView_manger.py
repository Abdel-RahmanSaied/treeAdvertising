from PyQt5 import QtWidgets , QtCore
from views import newOrder_view
import json
import requests
import os

class NewOrderView_manger(QtWidgets.QWidget, newOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    home_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(NewOrderView_manger, self).__init__()
        self.setupUi(self)
        self.otherKind_radioButton.toggled.connect(self.other_kind_lineEdit_2.setEnabled)
        self.clientDesign_btn.clicked.connect(self.getdesign_path)
        self.upload_photo_btn.clicked.connect(self.getphoto_path)
        self.search_btn.clicked.connect(self.check_client)
        self.save_btn.clicked.connect(self.add_new_order)

        self.client_check_url = 'https://saied.pythonanywhere.com/clientPhone/'
        self.add_client_url = 'https://saied.pythonanywhere.com/clients/'
        self.orders_url = 'https://saied.pythonanywhere.com/orders/'

        self.token = '70d541af9b5dd9b1fb33ce325f0a90743d59f2ab'
        self.headers = {}

        '''
        data
        '''
        self.username = ''
        self.Orderid = 0
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
        self.target_dapertment = []
        self.cliend_id = -1

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
                print(check_reply)
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
                    # print(check_reply)
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
            self.headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json','Authorization': f'Token {self.token}'}
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
            self.Orderid = int(self.order_ID.text())

            if self.wood_radioButton.isChecked():
                self.materials = "خشب"
            elif self.plastic_radioButton.isChecked():
                self.materials = "بلاستيك"
            elif self.paper_radioButton.isChecked():
                self.materials = "ورق"
            elif self.otherKind_radioButton.isChecked() and len(self.other_kind_lineEdit_2.text()) != 0 :
                self.materials = self.other_kind_lineEdit_2.text()
            else:
                self.materials = "no material"

            self.thickness = float(self.thickness_doubleSpinBox.text())

            if len(self.color_lineEdit.text()) != 0:
                self.color = self.color_lineEdit.text()
            else:
                self.color = "no color"

            if self.shriek_checkBox.isChecked():
                self.Post_print_services.append("شرشرة")

            if self.rijah_checkBox.isChecked():
                self.Post_print_services.append("ريجه")

            if self.thermalPackaging_checkBox.isChecked():
                self.Post_print_services.append("تغليف حرارى")

            if self.cut_checkBox.isChecked():
                self.Post_print_services.append("قص")

            if self.wood_checkBox_2.isChecked():
                self.Post_print_services.append("تجميع خشب")

            if self.Peel_checkBox.isChecked():
                self.Post_print_services.append("بشر")

            if self.binding_checkBox.isChecked():
                self.Post_print_services.append("تجليد")

            if self.packaging_checkBox.isChecked():
                self.Post_print_services.append("تعبئة و تغليف")

            if self.pin_checkBox.isChecked():
                self.Post_print_services.append("دبوس")

            if self.Spot_checkBox.isChecked():
                self.Post_print_services.append("اسبوت")

            if self.purpura_checkBox.isChecked():
                self.Post_print_services.append("فرفرية")

            if self.fingerprint_checkBox.isChecked():
                self.Post_print_services.append("بصمة")

            if self.kofrag_checkBox.isChecked():
                self.Post_print_services.append("كوفراج")

            if self.cutRokneh_checkBox.isChecked():
                self.Post_print_services.append("قص روكنه")

            if self.perforation_checkBox.isChecked():
                self.Post_print_services.append("تخريم")

            if self.idPerforatio_checkBox.isChecked():
                self.Post_print_services.append("شرشرة id")

            if self.circularCut_checkBox.isChecked():
                self.Post_print_services.append("قص دائرى")

            if int(self.wire_spinBox.text()) != 0:
                self.Post_print_services.append(f" سلك{self.wire_spinBox.text()}")

            self.Post_print_services.append(f"سلوفان {self.cellophane_comboBox.currentText()} ")

            self.state = 'D'

            if len(self.notes_textEdit.toPlainText()) != 0 :
                self.notes = self.notes_textEdit.toPlainText()
            else:
                self.notes = "nothing"

            if self.design_checkBox.isChecked() :
                self.target_dapertment.append("D")
            if self.printing_checkBox.isChecked() :
                self.target_dapertment.append("P")

            """ Check Input Data """
            if self.design_types == '':
                msg.setWindowTitle("Warning")
                msg.setText("You must choose design type !")
                msg.exec_()
                self.design_category = []
                self.printing_type = []
                self.Post_print_services = []
                self.target_dapertment = []
            else:
                if len(self.target_dapertment) == 0:
                    msg.setWindowTitle("warning")
                    msg.setText("you must select at least one department.")
                    msg.exec_()
                    self.design_category = []
                    self.printing_type = []
                    self.Post_print_services = []
                    self.target_dapertment = []

                else:
                    ''' Client cheacker '''
                    if len(self.username_lin_3.text()) != 0:
                        if len(self.phone_number_lin.text()) != 0:
                            self.username = self.username_lin_3.text()
                            self.phone_number = self.phone_number_lin.text()

                            """-----------------"""
                            try:
                                if self.redRadioButton.isChecked():
                                    self.level = "R"
                                elif self.blueRadioButton.isChecked():
                                    self.level = "B"
                                elif self.greenRadioButton.isChecked():
                                    self.level = "G"
                            except Exception as r:
                                print(r)

                            self.recived_date = self.recived_date_lin.text()
                            self.post_date = self.post_date_lin.text()

                            client_data = {
                                "name": self.username,
                                "phone_number": self.phone_number,
                                "clientlevel": self.level
                            }

                            """ Post Order """
                            orderData = {
                                "order_id": self.Orderid,
                                "accepted_by": "Not Accepted yet",
                                "img_path": self.img_path,
                                "recived_date": self.recived_date,
                                "delivery_date": self.post_date,
                                "design_types": self.design_types,
                                "design_path": self.design_path,
                                "design_category": self.design_category,
                                "printing_type": self.printing_type,
                                "size_width": self.size_width,
                                "size_high": self.size_high,
                                "materials": self.materials,
                                "color": self.color,
                                "thickness": self.thickness,
                                "Post_print_services": self.Post_print_services,
                                "state": self.state,
                                "notes": self.notes,
                                "client_id": self.cliend_id,
                                "target_dapertment": self.target_dapertment

                            }

                            try:
                                if self.cliend_id != -1:

                                    self.check_reply = requests.post(self.orders_url, json=orderData,
                                                                     headers=self.headers).json()
                                    print(self.check_reply)
                                    try :
                                        self.check_reply["Response"] == 'invalid data'
                                        msg.setWindowTitle("successfully")
                                        msg.setText("order id already exsist !.")
                                        msg.exec_()
                                        self.design_category = []
                                        self.printing_type = []
                                        self.Post_print_services = []
                                        self.target_dapertment = []
                                    except :
                                        self.checkAcceptedSignal.emit()
                                        msg.setWindowTitle("successfully")
                                        msg.setText("your request sent successfully.")
                                        msg.exec_()
                                else:
                                    add_client_reply = requests.post(self.add_client_url, json=client_data,
                                                                     headers=self.headers).json()
                                    self.cliend_id = add_client_reply['id']
                                    orderData["client_id"] = add_client_reply['id']
                                    # print(orderData)
                                    self.check_reply = requests.post(self.orders_url, json=orderData,
                                                                     headers=self.headers).json()
                                    # print("Respnse : ", self.check_reply)
                                    self.checkAcceptedSignal.emit()
                                    msg.setWindowTitle("successfully")
                                    msg.setText("your request sent successfully.")
                                    msg.exec_()

                            except (requests.ConnectionError, requests.Timeout) as exception:
                                msg.setWindowTitle("Warning")
                                msg.setText("No internet connection.")
                                msg.exec_()
                            except Exception as e:
                                #print(e)
                                msg.setWindowTitle("Warning")
                                msg.setText(
                                    "The phone number is already registered with another client  , you can use search button.")
                                msg.exec_()


                        else:
                            msg.setWindowTitle("Warning")
                            msg.setText("You must enter phone number.")
                            msg.exec_()
                            self.design_category = []
                            self.printing_type = []
                            self.Post_print_services = []
                            self.target_dapertment = []
                    else:
                        msg.setWindowTitle("Warning")
                        msg.setText("You must enter user name.")
                        msg.exec_()
                        self.design_category = []
                        self.printing_type = []
                        self.Post_print_services = []
                        self.target_dapertment = []

        except Exception as e:
            print(e)


    def clear_data(self):
        self.username_lin_3.setText("")
        self.phone_number_lin.setText("")
        # self.redRadioButton.setChecked(False)
        # self.blueRadioButton.setChecked(False)
        # self.greenRadioButton.setChecked(False)
        self.recived_date_lin.date()
        self.post_date_lin.date()
        # self.ofice_design.setChecked(False)
        # self.attatched_design.setChecked(False)
        self.filaPath_lbl.setText("مسار الملف")
        self.filaPath_lbl_2.setText("مسار الملف")
        self.certificate_checkBox.setChecked(False)
        self.cover_checkBox.setChecked(False)
        self.poster_checkBox.setChecked(False)
        self.rollUp_checkBox.setChecked(False)
        self.label_checkBox.setChecked(False)
        self.brochure_checkBox.setChecked(False)
        self.menu_checkBox.setChecked(False)
        self.flyer_checkBox.setChecked(False)
        self.logo_checkBox.setChecked(False)
        self.businessCard_checkBox.setChecked(False)
        self.banner_checkBox.setChecked(False)
        self.other_lineEdit.setText("")

        self.digital_checkBox.setChecked(False)
        self.indoor_checkBox.setChecked(False)
        self.outdoor_checkBox.setChecked(False)
        self.fiber_checkBox.setChecked(False)
        self.offset_checkBox.setChecked(False)
        self.selmation_checkBox.setChecked(False)
        self.silkscreen_checkBox.setChecked(False)
        self.flexo_checkBox.setChecked(False)
        self.Cutter_checkBox.setChecked(False)
        self.uv_checkBox.setChecked(False)
        self.laser_checkBox.setChecked(False)
        self.inkjet_checkBox.setChecked(False)

        self.high_doubleSpinBox.setValue(0.0)
        self.width_doubleSpinBox.setValue(0.0)
        self.thickness_doubleSpinBox.setValue(0.0)
        self.other_kind_lineEdit_2.setText("")
        self.color_lineEdit.setText("")

        self.shriek_checkBox.setChecked(False)
        self.wood_checkBox_2.setChecked(False)
        self.pin_checkBox.setChecked(False)
        self.cutRokneh_checkBox.setChecked(False)
        self.rijah_checkBox.setChecked(False)
        self.Peel_checkBox.setChecked(False)
        self.Spot_checkBox.setChecked(False)
        self.perforation_checkBox.setChecked(False)
        self.thermalPackaging_checkBox.setChecked(False)
        self.binding_checkBox.setChecked(False)
        self.purpura_checkBox.setChecked(False)
        self.idPerforatio_checkBox.setChecked(False)
        self.cut_checkBox.setChecked(False)
        self.packaging_checkBox.setChecked(False)
        self.fingerprint_checkBox.setChecked(False)
        self.circularCut_checkBox.setChecked(False)
        self.kofrag_checkBox.setChecked(False)
        self.design_checkBox.setChecked(False)
        self.printing_checkBox.setChecked(False)
        self.wire_spinBox.setValue(0)
        self.notes_textEdit.setText("")

        self.design_category = []
        self.printing_type = []
        self.Post_print_services = []
        self.target_dapertment = []




if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = NewOrderView_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()