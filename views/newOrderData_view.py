# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/newOrderData_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(989, 656)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(386, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(384, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(384, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        self.next_btn = QtWidgets.QPushButton(Form)
        self.next_btn.setMinimumSize(QtCore.QSize(0, 60))
        self.next_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.next_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.next_btn.setObjectName("next_btn")
        self.gridLayout_2.addWidget(self.next_btn, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(386, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_2.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_2.addWidget(self.checkBox_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"font: 11pt \"Acumin Pro\";\n"
"padding-bottom:7px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_5)
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"font: 11pt \"Acumin Pro\";\n"
"padding-bottom:7px;")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.color_listWidget = QtWidgets.QListWidget(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.color_listWidget.setFont(font)
        self.color_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.color_listWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.color_listWidget.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"font: 11pt \"Acumin Pro\";\n"
"padding-bottom:7px;")
        self.color_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.color_listWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.color_listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.color_listWidget.setObjectName("color_listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget.addItem(item)
        self.gridLayout_3.addWidget(self.color_listWidget, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.color_listWidget_2 = QtWidgets.QListWidget(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.color_listWidget_2.setFont(font)
        self.color_listWidget_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.color_listWidget_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.color_listWidget_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"font: 11pt \"Acumin Pro\";\n"
"padding-bottom:7px;")
        self.color_listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.color_listWidget_2.setTextElideMode(QtCore.Qt.ElideLeft)
        self.color_listWidget_2.setViewMode(QtWidgets.QListView.ListMode)
        self.color_listWidget_2.setObjectName("color_listWidget_2")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.color_listWidget_2.addItem(item)
        self.gridLayout_4.addWidget(self.color_listWidget_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 0, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clientDesign_rad_btn = QtWidgets.QRadioButton(self.groupBox_2)
        self.clientDesign_rad_btn.setMinimumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clientDesign_rad_btn.setFont(font)
        self.clientDesign_rad_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clientDesign_rad_btn.setStyleSheet("font: 15pt \"Acumin Pro\";")
        self.clientDesign_rad_btn.setText("")
        self.clientDesign_rad_btn.setIconSize(QtCore.QSize(30, 30))
        self.clientDesign_rad_btn.setObjectName("clientDesign_rad_btn")
        self.horizontalLayout.addWidget(self.clientDesign_rad_btn)
        self.clientDesign_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.clientDesign_btn.setMinimumSize(QtCore.QSize(110, 40))
        self.clientDesign_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.clientDesign_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.clientDesign_btn.setObjectName("clientDesign_btn")
        self.horizontalLayout.addWidget(self.clientDesign_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.filaPath_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.filaPath_lbl.setMinimumSize(QtCore.QSize(215, 0))
        self.filaPath_lbl.setMaximumSize(QtCore.QSize(16777215, 30))
        self.filaPath_lbl.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"font: 8pt \"Acumin Pro\";\n"
"padding-bottom:7px;")
        self.filaPath_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.filaPath_lbl.setObjectName("filaPath_lbl")
        self.horizontalLayout.addWidget(self.filaPath_lbl)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.clientDesign_rad_btn_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.clientDesign_rad_btn_2.setMinimumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clientDesign_rad_btn_2.setFont(font)
        self.clientDesign_rad_btn_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clientDesign_rad_btn_2.setStyleSheet("font: 15pt \"Acumin Pro\";")
        self.clientDesign_rad_btn_2.setText("")
        self.clientDesign_rad_btn_2.setIconSize(QtCore.QSize(30, 30))
        self.clientDesign_rad_btn_2.setObjectName("clientDesign_rad_btn_2")
        self.horizontalLayout_4.addWidget(self.clientDesign_rad_btn_2)
        self.officeDesign_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.officeDesign_btn.setMinimumSize(QtCore.QSize(110, 40))
        self.officeDesign_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.officeDesign_btn.setStyleSheet("font: 11pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(50, 85, 127);\n"
"\n"
" border-radius: 12px;\n"
"")
        self.officeDesign_btn.setObjectName("officeDesign_btn")
        self.horizontalLayout_4.addWidget(self.officeDesign_btn)
        spacerItem6 = QtWidgets.QSpacerItem(233, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 3)

        self.retranslateUi(Form)
        self.clientDesign_btn.clicked.connect(self.clientDesign_rad_btn.click) # type: ignore
        self.officeDesign_btn.clicked.connect(self.clientDesign_rad_btn_2.click) # type: ignore
        self.officeDesign_btn.clicked.connect(self.filaPath_lbl.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.next_btn.setText(_translate("Form", "التالي"))
        self.label.setText(_translate("Form", "أمر شغل جديد"))
        self.groupBox.setTitle(_translate("Form", "بيانات امر الشغل"))
        self.groupBox_5.setTitle(_translate("Form", "خدمات ما بعد الطباعه"))
        self.checkBox_6.setText(_translate("Form", "شرشره تخريم"))
        self.checkBox_7.setText(_translate("Form", "تغليف"))
        self.checkBox_8.setText(_translate("Form", "تجميع خشب"))
        self.checkBox_9.setText(_translate("Form", "تجليد"))
        self.label_3.setText(_translate("Form", "سلوفان"))
        self.comboBox.setItemText(0, _translate("Form", "مط"))
        self.comboBox.setItemText(1, _translate("Form", "لامع"))
        self.label_4.setText(_translate("Form", "سلك"))
        self.checkBox.setText(_translate("Form", "ريجه"))
        self.checkBox_5.setText(_translate("Form", "قص"))
        self.checkBox_3.setText(_translate("Form", "بشر"))
        self.checkBox_2.setText(_translate("Form", "تغليف حراري"))
        self.checkBox_4.setText(_translate("Form", "دبوس"))
        self.groupBox_3.setTitle(_translate("Form", "أنواع الطباعه"))
        __sortingEnabled = self.color_listWidget.isSortingEnabled()
        self.color_listWidget.setSortingEnabled(False)
        item = self.color_listWidget.item(0)
        item.setText(_translate("Form", "ديجيتال"))
        item = self.color_listWidget.item(1)
        item.setText(_translate("Form", "اوفسيت"))
        item = self.color_listWidget.item(2)
        item.setText(_translate("Form", "سلك سكرين"))
        item = self.color_listWidget.item(3)
        item.setText(_translate("Form", "بنر"))
        item = self.color_listWidget.item(4)
        item.setText(_translate("Form", "Uv"))
        item = self.color_listWidget.item(5)
        item.setText(_translate("Form", "ليزر"))
        item = self.color_listWidget.item(6)
        item.setText(_translate("Form", "فايبر"))
        item = self.color_listWidget.item(7)
        item.setText(_translate("Form", "سبلميشن"))
        item = self.color_listWidget.item(8)
        item.setText(_translate("Form", "انك جيت"))
        self.color_listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("Form", "الخامات"))
        __sortingEnabled = self.color_listWidget_2.isSortingEnabled()
        self.color_listWidget_2.setSortingEnabled(False)
        item = self.color_listWidget_2.item(0)
        item.setText(_translate("Form", "خشب"))
        item = self.color_listWidget_2.item(1)
        item.setText(_translate("Form", "ورق"))
        item = self.color_listWidget_2.item(2)
        item.setText(_translate("Form", "بلاستيك"))
        self.color_listWidget_2.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("Form", "التصميم"))
        self.clientDesign_btn.setText(_translate("Form", "تصميم العميل"))
        self.filaPath_lbl.setText(_translate("Form", "مسار الملف"))
        self.officeDesign_btn.setText(_translate("Form", "تصميم بالمكتب"))
