# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/orderRequirment_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1340, 810)
        Form.setMinimumSize(QtCore.QSize(1340, 810))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(550, 20, 271, 51))
        self.label.setMaximumSize(QtCore.QSize(271, 71))
        font = QtGui.QFont()
        font.setFamily("Thunder Lord")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(50, 70, 1271, 651))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.details_btn = QtWidgets.QPushButton(Form)
        self.details_btn.setGeometry(QtCore.QRect(720, 730, 200, 60))
        self.details_btn.setMinimumSize(QtCore.QSize(200, 60))
        self.details_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.details_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.details_btn.setObjectName("details_btn")
        self.bck_btn = QtWidgets.QPushButton(Form)
        self.bck_btn.setGeometry(QtCore.QRect(410, 730, 200, 60))
        self.bck_btn.setMinimumSize(QtCore.QSize(200, 60))
        self.bck_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.bck_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.bck_btn.setObjectName("bck_btn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1361, 821))
        self.label_3.setMinimumSize(QtCore.QSize(1361, 821))
        self.label_3.setMaximumSize(QtCore.QSize(1361, 821))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/login/images/30663.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.details_btn.raise_()
        self.bck_btn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "متطلبات اوامر الشغل"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "اسم الطلب"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "الكميه"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "اسم الطالب"))
        self.details_btn.setText(_translate("Form", "انتهي"))
        self.bck_btn.setText(_translate("Form", "الرجوع"))
import app_resources_rc
