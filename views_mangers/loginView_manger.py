from PyQt5 import QtWidgets , QtCore
from views import login_view
import json
import os

class Login_Manager(QtWidgets.QWidget, login_view.Ui_login):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Login_Manager, self).__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.handle_login)

    def handle_login(self):
        import os
        # os.chdir("../")
        # db_path = os.path.join("database", "users_db.json")
        # msg = QtWidgets.QMessageBox()
        user_name = self.username_lin.text()
        password = self.password_lin.text()

        # try:
        #     if os.path.isfile(db_path):
        #         with open(db_path, 'r') as j:
        #             db = json.loads(j.read())
        #
        #         if len(user_name) == 0:
        #             msg.setWindowTitle("Warning")
        #             msg.setText("the user name and password can't be empty  ")
        #             msg.exec_()
        #         elif len(password) == 0:
        #             msg.setWindowTitle("Warning")
        #             msg.setText("the password can't be empty  ")
        #             msg.exec_()
        #
        #         elif user_name in db.keys():
        #             if password == db[user_name]["password"]:
        #                 self.loginAcceptedSignal.emit()
        #             else:
        #                 msg.setWindowTitle("Warning")
        #                 msg.setText("The password was invalid")
        #                 msg.exec_()
        #         else:
        #             msg.setWindowTitle("Warning")
        #             msg.setText("The User name was invalid")
        #             msg.exec_()
        # except:
        #     # msg.setWindowTitle("Warning")
        #     # msg.setText("Can't load database ")
        #     # msg.exec_()
        #     pass

        self.loginAcceptedSignal.emit()

    def clear(self):
        self.username_lin.setText("")
        self.password_lin.setText("")


if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = Login_Manager()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()