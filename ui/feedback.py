# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 335)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.bug_checkBox = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bug_checkBox.sizePolicy().hasHeightForWidth())
        self.bug_checkBox.setSizePolicy(sizePolicy)
        self.bug_checkBox.setObjectName("bug_checkBox")
        self.horizontalLayout.addWidget(self.bug_checkBox)
        self.suggestion_checkBox = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suggestion_checkBox.sizePolicy().hasHeightForWidth())
        self.suggestion_checkBox.setSizePolicy(sizePolicy)
        self.suggestion_checkBox.setObjectName("suggestion_checkBox")
        self.horizontalLayout.addWidget(self.suggestion_checkBox)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.write_textEdit = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.write_textEdit.sizePolicy().hasHeightForWidth())
        self.write_textEdit.setSizePolicy(sizePolicy)
        self.write_textEdit.setObjectName("write_textEdit")
        self.verticalLayout.addWidget(self.write_textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.submit_pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_pushButton.sizePolicy().hasHeightForWidth())
        self.submit_pushButton.setSizePolicy(sizePolicy)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.horizontalLayout_2.addWidget(self.submit_pushButton)
        self.info_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sizePolicy)
        self.info_label.setText("")
        self.info_label.setObjectName("info_label")
        self.horizontalLayout_2.addWidget(self.info_label)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "问题类型"))
        self.bug_checkBox.setText(_translate("Form", "BUG反馈"))
        self.suggestion_checkBox.setText(_translate("Form", "优化建议"))
        self.submit_pushButton.setText(_translate("Form", "提交问题"))
