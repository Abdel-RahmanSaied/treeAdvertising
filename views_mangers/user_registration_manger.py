from PyQt5 import QtWidgets , QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from views import user_registration_view
import requests



class Registration_manger(QtWidgets.QWidget, user_registration_view.Ui_Form):

    def __init__(self , name=None, *args, **kwargs ):
        super(Registration_manger, self).__init__()
        self.setupUi(self)
        self.base_url = 'https://saied.pythonanywhere.com/register/'
        self.token = '009ae49af6e4afacec65273b6a97849e3f443792'

        self.add_btn.clicked.connect(self.run)


    def run(self):
        msg = QtWidgets.QMessageBox()
        headers = {'Accept': 'application/json; indent=4', 'Content-Type': 'application/json',
                   'Authorization': f'Token {self.token}'}

        name = ''
        user_name = ''
        department = ''
        password_1 = ''
        password_2 = ''

        if len(self.name_lin.text()) != 0 :
            if len(self.username_lin.text()) != 0 :
                if len(self.password_1_lin.text()) != 0 :
                    if len(self.password_2_lin.text()) != 0:
                        if self.password_1_lin.text() == self.password_2_lin.text() :

                            try:
                                if self.manger_Rad.isChecked():
                                    department = "M"
                                elif self.designer_Rad.isChecked():
                                    department= "D"
                                elif self.printer_Rad.isChecked():
                                    department = "P"
                                else:
                                    msg.setWindowTitle("Warning")
                                    msg.setText("You must select the department.")
                                    msg.exec_()
                            except Exception as r:
                                print(r)

                            name = self.name_lin.text()
                            user_name = self.username_lin.text()
                            password_1 = str(self.password_1_lin.text())
                            password_2 = str(self.password_2_lin.text())

                        else:
                            msg.setWindowTitle("Warning")
                            msg.setText("the password and confirm password not the same !! .")
                            msg.exec_()

                    else:
                        msg.setWindowTitle("Warning")
                        msg.setText("You must confirm the password.")
                        msg.exec_()

                else:
                    msg.setWindowTitle("Warning")
                    msg.setText("You must enter the password.")
                    msg.exec_()



            else:
                msg.setWindowTitle("Warning")
                msg.setText("You must enter the user name.")
                msg.exec_()
        else:
            msg.setWindowTitle("Warning")
            msg.setText("You must enter the name.")
            msg.exec_()

        data = {
    "name": name,
    "username": user_name,
    "department": department,
    "password1": password_1,
    "password2": password_2
}
        print(data)
        try:
            self.reply = requests.post(self.base_url, json = data,  headers=headers).json()
            if self.reply['Response'] =='Successful created' :
                msg.setWindowTitle("Successfully")
                msg.setText("Successful created ")
                msg.exec_()
            else:
                msg.setWindowTitle("Failed")
                msg.setText("You don't have any permision to do that")
                msg.exec_()
        except Exception as s:
            print("ss", s)
    def clear(self):
        pass


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Registration_manger()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()