from PyQt5 import QtWidgets , QtCore
from PyQt5.QtCore import QDate

from views import editOrder_view
import json
import requests
import os

class EditOrderView_manger(QtWidgets.QWidget, editOrder_view.Ui_Form):
    checkAcceptedSignal = QtCore.pyqtSignal()
    home_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(EditOrderView_manger, self).__init__()
        self.setupUi(self)
        self.otherKind_radioButton.toggled.connect(self.other_kind_lineEdit_2.setEnabled)
        self.clientDesign_btn.clicked.connect(self.getdesign_path)
        self.upload_photo_btn.clicked.connect(self.getphoto_path)

        #self.save_btn.clicked.connect(self.add_new_order)

        self.orders_url = 'https://saied.pythonanywhere.com/orders/'
        self.update_link = "https://saied.pythonanywhere.com/updateItem/"

        self.token = '70d541af9b5dd9b1fb33ce325f0a90743d59f2ab'
        self.headers = {}
    #     self.order = {
    #     "order_id": 9999,
    #     "user_name": "d",
    #     "client_name": "saieed",
    #     "accepted_by": "Not Accepted yet",
    #     "img_path": "no file selected",
    #     "date": "2022-06-28",
    #     "recived_date": "2027-06-06",
    #     "delivery_date": "2025-06-06",
    #     "design_types": "O",
    #     "design_path": "no file selected",
    #     "design_category": [
    #         "logo",
    #         "business Card",
    #         "banner",
    #         "brochure",
    #         "menu",
    #         "flyer",
    #         "certificate",
    #         "cover",
    #         "poster",
    #         "RollUp",
    #         "label",
    #         "wwwwww"
    #     ],
    #     "printing_type": [
    #         "ديجيتال",
    #         "اوفسيت",
    #         "سلك سكرين",
    #         "UV",
    #         "ان دور",
    #         "اوت دور",
    #         "فلكسو",
    #         "ليزر",
    #         "فايبر",
    #         "سيلميشن",
    #         "كتر بلوتر",
    #         "انك جيت"
    #     ],
    #     "size_width": 3.0,
    #     "size_high": 3.0,
    #     "materials": "dddd",
    #     "color": "www",
    #     "thickness": 3.0,
    #     "Post_print_services": [
    #         "شرشرة",
    #         "ريجه",
    #         "تغليف حرارى",
    #         "قص",
    #         "تجميع خشب",
    #         "بشر",
    #         "تجليد",
    #         "تعبئة و تغليف",
    #         "دبوس",
    #         "اسبوت",
    #         "فرفرية",
    #         "بصمة",
    #         "كوفراج",
    #         "قص روكنه",
    #         "تخريم",
    #         "شرشرة id",
    #         "قص دائرى",
    #         " سلك2",
    #         "سلوفان لامع "
    #     ],
    #     "state": "F",
    #     "notes": "wwwwwww",
    #     "target_dapertment": [
    #         "D",
    #         "P"
    #     ],
    #     "user_id": 7,
    #     "client_id": 3
    # }

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
        self.order = {}

    def run(self):
        msg = QtWidgets.QMessageBox()
        try :
            self.headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                            'Authorization': f'Token {self.token}'}
        except Exception as j :
            print("j",j)
        try:
            self.reply = requests.get(self.orders_url,  headers=self.headers).json()
            for item in self.reply :
                if item["order_id"] == self.Orderid :
                    self.order = item
                    break

        except Exception as d:
            print("dd",d)

        try :
            self.cliend_id = self.order["client_id"]
            self.username_lin_3.setText(self.order['client_name'])
            self.recived_date_lin.setDate(QDate.fromString(self.order['recived_date']))
            self.post_date_lin.setDate(QDate.fromString(self.order['delivery_date']))

            if self.design_types == "O" :
                self.ofice_design.setChecked(True)
            elif self.design_types == 'A':
                self.attatched_design.setChecked(True)
            self.filaPath_lbl.setText(self.order['design_path'])
            self.filaPath_lbl_2.setText(self.order['img_path'])
            if "logo" in self.order['design_category']:
                self.logo_checkBox.setChecked(True)

            if "business Card" in self.order['design_category']:
                self.businessCard_checkBox.setChecked(True)

            if "banner" in self.order['design_category']:
                self.banner_checkBox.setChecked(True)

            if "brochure" in self.order['design_category']:
                self.brochure_checkBox.setChecked(True)

            if "menu" in self.order['design_category']:
                self.menu_checkBox.setChecked(True)

            if "flyer" in self.order['design_category']:
                self.flyer_checkBox.setChecked(True)

            if "certificate" in self.order['design_category']:
                self.certificate_checkBox.setChecked(True)

            if "cover" in self.order['design_category']:
                self.cover_checkBox.setChecked(True)

            if "poster" in self.order['design_category']:
                self.poster_checkBox.setChecked(True)

            if "RollUp" in self.order['design_category']:
                self.rollUp_checkBox.setChecked(True)

            if "label" in self.order['design_category']:
                self.label_checkBox.setChecked(True)

            if self.order['design_category'][-1] not in ["logo","business Card","banner","brochure","menu","flyer","certificate","cover","poster","RollUp","label"]:
                self.other_lineEdit.setText(self.order['design_category'][-1])

            if "ديجيتال" in self.order['printing_type']:
                self.digital_checkBox.setChecked(True)

            if "اوفسيت" in self.order['printing_type']:
                self.offset_checkBox.setChecked(True)

            if "سلك سكرين" in self.order['printing_type']:
                self.silkscreen_checkBox.setChecked(True)

            if "UV" in self.order['printing_type']:
                self.uv_checkBox.setChecked(True)

            if "ان دور" in self.order['printing_type']:
                self.indoor_checkBox.setChecked(True)

            if "اوت دور" in self.order['printing_type']:
                self.outdoor_checkBox.setChecked(True)

            if "فلكسو" in self.order['printing_type']:
                self.flexo_checkBox.setChecked(True)

            if "ليزر" in self.order['printing_type']:
                self.laser_checkBox.setChecked(True)

            if "فايبر" in self.order['printing_type']:
                self.fiber_checkBox.setChecked(True)

            if "سيلميشن" in self.order['printing_type']:
                self.selmation_checkBox.setChecked(True)

            if "كتر بلوتر" in self.order['printing_type']:
                self.Cutter_checkBox.setChecked(True)

            if "انك جيت" in self.order['printing_type']:
                self.inkjet_checkBox.setChecked(True)

            self.high_doubleSpinBox.setValue(self.order['size_high'])
            self.width_doubleSpinBox.setValue(self.order['size_width'])
            self.order_ID.setValue(self.order['order_id'])

            if self.order['materials'] == "خشب":
                self.wood_radioButton.setChecked(True)
            elif self.order['materials'] =="بلاستيك":
                self.plastic_radioButton.setChecked(True)
            elif self.order['materials'] =="ورق":
                self.paper_radioButton.setChecked(True)
            else:
                self.other_kind_lineEdit_2.setText(self.order['materials'])
                self.otherKind_radioButton.setChecked(True)

            self.thickness_doubleSpinBox.setValue(self.order['thickness'])
            self.color_lineEdit.setText(self.order['color'])

            for element in self.order['Post_print_services']:
                if "شرشرة" == element :
                    self.shriek_checkBox.setChecked(True)

                if "ريجه" == element :
                    self.rijah_checkBox.setChecked(True)

                if "تغليف حرارى" == element :
                    self.thermalPackaging_checkBox.setChecked(True)

                if "قص" == element :
                    self.cut_checkBox.setChecked(True)

                if "تجميع خشب" == element :
                    self.wood_checkBox_2.setChecked(True)

                if "بشر" == element :
                    self.Peel_checkBox.setChecked(True)

                if "تجليد" == element :
                    self.binding_checkBox.setChecked(True)

                if "تعبئة و تغليف" == element :
                    self.packaging_checkBox.setChecked(True)

                if "دبوس" == element :
                    self.pin_checkBox.setChecked(True)

                if "اسبوت" == element :
                    self.Spot_checkBox.setChecked(True)

                if "فرفرية" == element :
                    self.purpura_checkBox.setChecked(True)

                if "بصمة" == element :
                    self.fingerprint_checkBox.setChecked(True)

                if "كوفراج" == element :
                    self.kofrag_checkBox.setChecked(True)

                if "قص روكنه" == element :
                    self.cutRokneh_checkBox.setChecked(True)

                if "تخريم" == element :
                    self.perforation_checkBox.setChecked(True)

                if "شرشرة id" == element :
                    self.idPerforatio_checkBox.setChecked(True)

                if "قص دائرى" == element:
                    self.circularCut_checkBox.setChecked(True)

                if "سلك" in element :
                    self.wire_spinBox.setValue(int(''.join(filter(str.isdigit, element)) ))

                if "سلوفان" in element :
                    if "لامع" in element : self.cellophane_comboBox.setCurrentIndex(1)

            if self.order['state'] == "I" :
                self.cellophane_comboBox_2.setCurrentIndex(1)
            elif self.order['state'] == "F" :
                self.cellophane_comboBox_2.setCurrentIndex(2)

            if "P" in self.order['target_dapertment'] : self.printing_checkBox.setChecked(True)
            if "D" in self.order['target_dapertment']  : self.design_checkBox.setChecked(True)

            self.notes_textEdit.setText(self.order['notes'])

        except Exception as e:
            print(e)
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
                        # if len(self.phone_number_lin.text()) != 0:
                        self.username = self.username_lin_3.text()
                        self.phone_number = self.phone_number_lin.text()
                        print("xcxcxcxcxc")
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

                            self.update_reply = requests.put(f"{self.update_link}{self.Orderid}//" , json=orderData , headers=self.headers).json()

                            msg.setWindowTitle("Succesfully")
                            msg.setText(self.update_reply["Response"])
                            msg.exec_()
                        except Exception as rrr :
                            print(rrr)

        except Exception as e :
            print(e)

    def clear(self):
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
        self.order = {}


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = EditOrderView_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()