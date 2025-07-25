# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shortcut_keys.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 452)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.info_label_4.setObjectName("info_label_4")
        self.verticalLayout.addWidget(self.info_label_4)
        self.key_name_listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_name_listWidget.sizePolicy().hasHeightForWidth())
        self.key_name_listWidget.setSizePolicy(sizePolicy)
        self.key_name_listWidget.setObjectName("key_name_listWidget")
        self.verticalLayout.addWidget(self.key_name_listWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_label_5 = QtWidgets.QLabel(self.centralwidget)
        self.info_label_5.setObjectName("info_label_5")
        self.verticalLayout_2.addWidget(self.info_label_5)
        self.key_info_listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key_info_listWidget.sizePolicy().hasHeightForWidth())
        self.key_info_listWidget.setSizePolicy(sizePolicy)
        self.key_info_listWidget.setObjectName("key_info_listWidget")
        self.verticalLayout_2.addWidget(self.key_info_listWidget)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.insert_input_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insert_input_pushButton.sizePolicy().hasHeightForWidth())
        self.insert_input_pushButton.setSizePolicy(sizePolicy)
        self.insert_input_pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.insert_input_pushButton.setObjectName("insert_input_pushButton")
        self.horizontalLayout.addWidget(self.insert_input_pushButton)
        self.delete_key_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_key_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_key_pushButton.setSizePolicy(sizePolicy)
        self.delete_key_pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.delete_key_pushButton.setObjectName("delete_key_pushButton")
        self.horizontalLayout.addWidget(self.delete_key_pushButton)
        self.change_key_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_key_pushButton.sizePolicy().hasHeightForWidth())
        self.change_key_pushButton.setSizePolicy(sizePolicy)
        self.change_key_pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.change_key_pushButton.setObjectName("change_key_pushButton")
        self.horizontalLayout.addWidget(self.change_key_pushButton)
        self.change_enable_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_enable_pushButton.sizePolicy().hasHeightForWidth())
        self.change_enable_pushButton.setSizePolicy(sizePolicy)
        self.change_enable_pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.change_enable_pushButton.setObjectName("change_enable_pushButton")
        self.horizontalLayout.addWidget(self.change_enable_pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.delay_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delay_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.delay_doubleSpinBox.setSizePolicy(sizePolicy)
        self.delay_doubleSpinBox.setMinimumSize(QtCore.QSize(80, 0))
        self.delay_doubleSpinBox.setObjectName("delay_doubleSpinBox")
        self.horizontalLayout.addWidget(self.delay_doubleSpinBox)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 8)
        self.horizontalLayout.setStretch(3, 12)
        self.horizontalLayout.setStretch(4, 9)
        self.horizontalLayout.setStretch(5, 9)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_5.setStretch(0, 7)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_label = QtWidgets.QLabel(self.centralwidget)
        self.info_label.setText("")
        self.info_label.setWordWrap(True)
        self.info_label.setObjectName("info_label")
        self.verticalLayout_3.addWidget(self.info_label)
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setText("")
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        self.verticalLayout_3.addWidget(self.error_label)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.open_macro_command_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_macro_command_pushButton.sizePolicy().hasHeightForWidth())
        self.open_macro_command_pushButton.setSizePolicy(sizePolicy)
        self.open_macro_command_pushButton.setObjectName("open_macro_command_pushButton")
        self.verticalLayout_4.addWidget(self.open_macro_command_pushButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_pushButton.sizePolicy().hasHeightForWidth())
        self.submit_pushButton.setSizePolicy(sizePolicy)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.horizontalLayout_2.addWidget(self.submit_pushButton)
        self.close_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_pushButton.sizePolicy().hasHeightForWidth())
        self.close_pushButton.setSizePolicy(sizePolicy)
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout_2.addWidget(self.close_pushButton)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.software_update_action = QtWidgets.QAction(MainWindow)
        self.software_update_action.setObjectName("software_update_action")
        self.problem_feedback_action = QtWidgets.QAction(MainWindow)
        self.problem_feedback_action.setObjectName("problem_feedback_action")
        self.menu.addAction(self.software_update_action)
        self.menu.addAction(self.problem_feedback_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.info_label_4.setText(_translate("MainWindow", "快捷键列表"))
        self.info_label_5.setText(_translate("MainWindow", "快捷键内容"))
        self.insert_input_pushButton.setText(_translate("MainWindow", "新增"))
        self.delete_key_pushButton.setText(_translate("MainWindow", "删除"))
        self.change_key_pushButton.setText(_translate("MainWindow", "修改"))
        self.change_enable_pushButton.setText(_translate("MainWindow", "启用/禁用"))
        self.label.setText(_translate("MainWindow", "连续按键延时"))
        self.open_macro_command_pushButton.setText(_translate("MainWindow", "宏命令管理"))
        self.submit_pushButton.setText(_translate("MainWindow", "开启"))
        self.close_pushButton.setText(_translate("MainWindow", "关闭"))
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.software_update_action.setText(_translate("MainWindow", "软件更新"))
        self.problem_feedback_action.setText(_translate("MainWindow", "问题反馈"))
