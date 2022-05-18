# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/login_view.ui'
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
        Form.setMaximumSize(QtCore.QSize(1340, 810))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-21, -11, 1361, 821))
        self.label_3.setMinimumSize(QtCore.QSize(1361, 821))
        self.label_3.setMaximumSize(QtCore.QSize(1361, 821))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/login/images/30663.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(320, 50, 731, 691))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(200, 200))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/logo/images/logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 4)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.username_lin = QtWidgets.QLineEdit(self.groupBox)
        self.username_lin.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(10)
        self.username_lin.setFont(font)
        self.username_lin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username_lin.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.username_lin.setObjectName("username_lin")
        self.horizontalLayout_12.addWidget(self.username_lin)
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 2, 0, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 5, 3, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem6 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.password_lin = QtWidgets.QLineEdit(self.groupBox)
        self.password_lin.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(10)
        self.password_lin.setFont(font)
        self.password_lin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password_lin.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.password_lin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lin.setObjectName("password_lin")
        self.horizontalLayout_13.addWidget(self.password_lin)
        spacerItem7 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 4, 0, 1, 4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 83, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 3, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 83, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 7, 1, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem10 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem10)
        self.login_btn = QtWidgets.QPushButton(self.groupBox)
        self.login_btn.setMinimumSize(QtCore.QSize(221, 51))
        self.login_btn.setMaximumSize(QtCore.QSize(221, 51))
        self.login_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(1, 25, 54);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_14.addWidget(self.login_btn)
        spacerItem11 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 6, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username_lin.setPlaceholderText(_translate("Form", "E-Mail"))
        self.password_lin.setPlaceholderText(_translate("Form", "Password"))
        self.login_btn.setText(_translate("Form", " LOGIN"))
import app_resources_rc
