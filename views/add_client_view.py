# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/add_client_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1088)
        Form.setMinimumSize(QtCore.QSize(1340, 810))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 1920, 1080))
        self.label_3.setMinimumSize(QtCore.QSize(1920, 1080))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/login/images/backgroung/3433814.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(700, 100, 558, 836))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setMinimumSize(QtCore.QSize(60, 15))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_15.setStyleSheet("background-color: rgb(30,  160, 30);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setMaximumSize(QtCore.QSize(15, 16777215))
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_4.addWidget(self.radioButton_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(60, 15))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_12.setStyleSheet("background-color: rgb(20, 20, 200);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setMaximumSize(QtCore.QSize(15, 16777215))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(60, 15))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_13.setStyleSheet("background-color: rgb(200, 30, 30);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setMaximumSize(QtCore.QSize(15, 16777215))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 6, 0, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 83, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 7, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(152, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem6, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 1, 2, 2)
        spacerItem7 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 84, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem8, 5, 1, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem9 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.name_lin = QtWidgets.QLineEdit(self.groupBox)
        self.name_lin.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(10)
        self.name_lin.setFont(font)
        self.name_lin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_lin.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.name_lin.setInputMask("")
        self.name_lin.setText("")
        self.name_lin.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lin.setObjectName("name_lin")
        self.horizontalLayout_12.addWidget(self.name_lin)
        spacerItem10 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.gridLayout_5.addLayout(self.horizontalLayout_12, 2, 0, 1, 4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 83, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem11, 3, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem12 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.phone_lin = QtWidgets.QLineEdit(self.groupBox)
        self.phone_lin.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(10)
        self.phone_lin.setFont(font)
        self.phone_lin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.phone_lin.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.phone_lin.setText("")
        self.phone_lin.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.phone_lin.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_lin.setObjectName("phone_lin")
        self.horizontalLayout_13.addWidget(self.phone_lin)
        spacerItem13 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.gridLayout_5.addLayout(self.horizontalLayout_13, 4, 0, 1, 4)
        spacerItem14 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem14, 9, 2, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem15 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem15)
        self.end_btn = QtWidgets.QPushButton(self.groupBox)
        self.end_btn.setMinimumSize(QtCore.QSize(183, 51))
        self.end_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.end_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(190, 20, 20,190);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.end_btn.setObjectName("end_btn")
        self.horizontalLayout_14.addWidget(self.end_btn)
        spacerItem16 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.add_btn = QtWidgets.QPushButton(self.groupBox)
        self.add_btn.setMinimumSize(QtCore.QSize(183, 51))
        self.add_btn.setMaximumSize(QtCore.QSize(300, 51))
        self.add_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(20,  190, 120);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_14.addWidget(self.add_btn)
        spacerItem17 = QtWidgets.QSpacerItem(58, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.gridLayout_5.addLayout(self.horizontalLayout_14, 10, 0, 1, 4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem18, 0, 0, 1, 1)
        self.notes_text = QtWidgets.QGroupBox(self.groupBox)
        self.notes_text.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.notes_text.setFont(font)
        self.notes_text.setAlignment(QtCore.Qt.AlignCenter)
        self.notes_text.setObjectName("notes_text")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.notes_text)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.notes_text)
        self.textEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.notes_text, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem19, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 8, 0, 1, 4)
        spacerItem20 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem20, 11, 0, 1, 1)
        self.exit_btn = QtWidgets.QPushButton(Form)
        self.exit_btn.setGeometry(QtCore.QRect(1870, 10, 30, 30))
        self.exit_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.exit_btn.setMaximumSize(QtCore.QSize(161, 161))
        self.exit_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(178, 39, 39,100);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.exit_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-close-window-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon)
        self.exit_btn.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn.setObjectName("exit_btn")
        self.minimize_btn = QtWidgets.QPushButton(Form)
        self.minimize_btn.setGeometry(QtCore.QRect(1820, 10, 30, 30))
        self.minimize_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.minimize_btn.setMaximumSize(QtCore.QSize(161, 161))
        self.minimize_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 229, 32,100);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.minimize_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-subtract-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_btn.setIcon(icon1)
        self.minimize_btn.setIconSize(QtCore.QSize(30, 30))
        self.minimize_btn.setObjectName("minimize_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "إضافة عميل جديد"))
        self.name_lin.setPlaceholderText(_translate("Form", "الأسم"))
        self.phone_lin.setPlaceholderText(_translate("Form", "رقم الهاتف"))
        self.end_btn.setText(_translate("Form", "إنهاء"))
        self.add_btn.setText(_translate("Form", "حفظ"))
        self.notes_text.setTitle(_translate("Form", "تفاصيل آخرى"))
import app_resources_rc
