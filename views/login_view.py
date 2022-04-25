# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/login_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(875, 641)
        self.gridLayout_3 = QtWidgets.QGridLayout(login)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(login)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.username_lin = QtWidgets.QLineEdit(self.groupBox)
        self.username_lin.setMinimumSize(QtCore.QSize(291, 0))
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
        self.horizontalLayout_7.addWidget(self.username_lin)
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 0, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 5, 3, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.password_lin = QtWidgets.QLineEdit(self.groupBox)
        self.password_lin.setMinimumSize(QtCore.QSize(291, 0))
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
        self.horizontalLayout_8.addWidget(self.password_lin)
        spacerItem7 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 0, 1, 4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 83, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 83, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 7, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
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
        self.horizontalLayout_6.addWidget(self.login_btn)
        spacerItem11 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 4)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.username_lin.setPlaceholderText(_translate("login", "E-Mail"))
        self.password_lin.setPlaceholderText(_translate("login", "Password"))
        self.login_btn.setText(_translate("login", " LOGIN"))
import app_resources_rc
