from PyQt5 import QtWidgets , QtGui , QtCore
from views_mangers.loginView_manger import  Login_Manager
from views_mangers.main_manger import Main_manger
from views_mangers.newOrderView_manger import NewOrderView_manger
from views_mangers.newOrderDataView_manger import NewOrderDataView_manger


class Tree_Advertising(QtWidgets.QStackedWidget):
    def __init__(self):
        super(Tree_Advertising, self).__init__()
        self.login_manger = Login_Manager()
        self.main_manger = Main_manger()
        self.newOrder_manger=NewOrderView_manger()
        self.newOrderData_manger=NewOrderDataView_manger()

        # add widgets to the stack
        self.addWidget(self.login_manger)
        self.addWidget(self.main_manger)
        self.addWidget(self.newOrder_manger)
        self.addWidget(self.newOrderData_manger)

        # install signals
        self.login_manger.loginAcceptedSignal.connect(self.handle_login_accepted)
        # self.main_manger.cs_btn.clicked.connect(self.handle_cs_process)
        '''
        main view signals
        '''
        self.main_manger.workOrder_btn.clicked.connect(self.handle_workOrder)

        '''
        new order view signals
        '''
        self.newOrder_manger.next_btn.clicked.connect(self.handle_newOrder)
        # self.predict_manager.back_btn.clicked.connect(lambda : self.setCurrentIndex(1))

    def handle_login_accepted(self):
        self.setCurrentIndex(1)
    def handle_workOrder(self):
        self.setCurrentIndex(2)
    def handle_newOrder(self):
        self.setCurrentIndex(3)


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = Tree_Advertising()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()










