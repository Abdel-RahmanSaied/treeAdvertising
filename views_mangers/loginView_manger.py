from PyQt5 import QtWidgets , QtCore
from views import login_view
import json
import requests

class Login_Manager(QtWidgets.QWidget, login_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Login_Manager, self).__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.handle_login)
        self.base_url = "https://saied.pythonanywhere.com/login/"
        self.userToken = ''

        self.setStyleSheet("\n"
                           "#Form {\n"
                           r"border-image: url(:E:\@projects\tree Advertising\treeAdvertising\forms\images\backgroung\3433814.jpg 0 0 0 0 stretch stretch;\n"
                           "}")

    def handle_login(self):
        msg = QtWidgets.QMessageBox()
        username = self.username_lin.text()
        password = self.password_lin.text()
        if len(username) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        elif len(password) == 0:
            msg.setWindowTitle("Warning")
            msg.setText("you must fill all fields !")
            msg.exec_()
        else:
            data = {
                    "username": username,
                    "password": password
                    }
            try:
                self.user_check = requests.post(self.base_url, data=data).json()
            except (requests.ConnectionError, requests.Timeout) as exception:
                print(exception)
                msg.setWindowTitle("Warning")
                msg.setText("No internet connection.")
                msg.exec_()
            try :
                for loginStatus in self.user_check.keys() :
                    if loginStatus == "non_field_errors" :
                        msg.setWindowTitle("Warning")
                        msg.setText("The user name or password was incorrect !")
                        msg.exec_()
                    elif loginStatus == "token" :
                        self.userToken = self.user_check[loginStatus]
                        # print(self.userToken)
                        self.loginAcceptedSignal.emit()
            except Exception as x :
                print(x)

    def clear(self):
        self.username_lin.setText("")
        self.password_lin.setText("")

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Login_Manager()
    w.show()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()