# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keys_combo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 215)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_list_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_list_label.sizePolicy().hasHeightForWidth())
        self.input_list_label.setSizePolicy(sizePolicy)
        self.input_list_label.setMinimumSize(QtCore.QSize(0, 20))
        self.input_list_label.setText("")
        self.input_list_label.setObjectName("input_list_label")
        self.verticalLayout.addWidget(self.input_list_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.input1_lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input1_lineEdit.sizePolicy().hasHeightForWidth())
        self.input1_lineEdit.setSizePolicy(sizePolicy)
        self.input1_lineEdit.setObjectName("input1_lineEdit")
        self.horizontalLayout.addWidget(self.input1_lineEdit)
        self.add1_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add1_label.sizePolicy().hasHeightForWidth())
        self.add1_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.add1_label.setFont(font)
        self.add1_label.setLineWidth(1)
        self.add1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add1_label.setObjectName("add1_label")
        self.horizontalLayout.addWidget(self.add1_label)
        self.input2_lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input2_lineEdit.sizePolicy().hasHeightForWidth())
        self.input2_lineEdit.setSizePolicy(sizePolicy)
        self.input2_lineEdit.setObjectName("input2_lineEdit")
        self.horizontalLayout.addWidget(self.input2_lineEdit)
        self.add2_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add2_label.sizePolicy().hasHeightForWidth())
        self.add2_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.add2_label.setFont(font)
        self.add2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.add2_label.setObjectName("add2_label")
        self.horizontalLayout.addWidget(self.add2_label)
        self.input3_lineEdit = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input3_lineEdit.sizePolicy().hasHeightForWidth())
        self.input3_lineEdit.setSizePolicy(sizePolicy)
        self.input3_lineEdit.setObjectName("input3_lineEdit")
        self.horizontalLayout.addWidget(self.input3_lineEdit)
        self.enable_checkBox = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.enable_checkBox.sizePolicy().hasHeightForWidth())
        self.enable_checkBox.setSizePolicy(sizePolicy)
        self.enable_checkBox.setObjectName("enable_checkBox")
        self.horizontalLayout.addWidget(self.enable_checkBox)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 3)
        self.horizontalLayout.setStretch(5, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.macro_name_comboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.macro_name_comboBox.sizePolicy().hasHeightForWidth())
        self.macro_name_comboBox.setSizePolicy(sizePolicy)
        self.macro_name_comboBox.setObjectName("macro_name_comboBox")
        self.horizontalLayout_2.addWidget(self.macro_name_comboBox)
        self.info_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        self.info_label.setText("")
        self.info_label.setObjectName("info_label")
        self.horizontalLayout_2.addWidget(self.info_label)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.delete_input_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_input_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_input_pushButton.setSizePolicy(sizePolicy)
        self.delete_input_pushButton.setObjectName("delete_input_pushButton")
        self.horizontalLayout_3.addWidget(self.delete_input_pushButton)
        self.save_input_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_input_pushButton.sizePolicy().hasHeightForWidth())
        self.save_input_pushButton.setSizePolicy(sizePolicy)
        self.save_input_pushButton.setObjectName("save_input_pushButton")
        self.horizontalLayout_3.addWidget(self.save_input_pushButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(5, 3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.add1_label.setText(_translate("Dialog", "+"))
        self.add2_label.setText(_translate("Dialog", "+"))
        self.enable_checkBox.setText(_translate("Dialog", "启用"))
        self.label.setText(_translate("Dialog", "连接宏命令"))
        self.delete_input_pushButton.setText(_translate("Dialog", "清除"))
        self.save_input_pushButton.setText(_translate("Dialog", "保存"))
