# -*- coding: utf-8 -*-
"""
Project Name: shortcut_keys
File Created: 2024.06.26
Author: ZhangYuetao
File Name: keys_insert.py
Update: 2025.04.24
"""

from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui, QtCore

import config
from ui.keys_combo import Ui_Dialog
import utils


class InputDialog(QDialog, Ui_Dialog):
    """
    快捷键输入对话框类，用于设置和管理快捷键组合及其对应的宏命令。

    Attributes:
        name (str): 快捷键名称。
        inputs (str): 快捷键组合。
        macro (str): 对应的宏命令名称。
        enable (bool): 快捷键是否启用。
        opened (str): 对话框的打开方式（'insert' 或 'change'）。
        parent (QWidget): 父窗口引用。
    """

    def __init__(self, parent=None, name=None, inputs=None, macro=None, enable=True, opened=None):
        """
        初始化快捷键输入对话框。

        :param parent: 父窗口对象，默认为 None。
        :param name: 快捷键名称，默认为 None。
        :param inputs: 快捷键组合，默认为 None。
        :param macro: 对应的宏命令名称，默认为 None。
        :param enable: 快捷键是否启用，默认为 True。
        :param opened: 对话框的打开方式（'insert' 或 'change'），默认为 None。
        """
        super(InputDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("快捷键输入")
        self.setWindowIcon(QtGui.QIcon(config.ICO_FILE))

        self.name = name
        self.inputs = inputs  # 输入快捷键组合
        self.macro = macro
        self.enable = enable  # 默认启用选项
        self.opened = opened
        if self.enable:
            self.enable_checkBox.click()  # 默认启用选项

        self.macro_name_comboBox.addItems(self.get_macro_name())

        # 连接按钮信号与槽函数
        self.buttonBox.accepted.connect(self.return_accept)
        self.buttonBox.rejected.connect(self.reject)
        self.delete_input_pushButton.clicked.connect(self.delete_input_line)
        self.enable_checkBox.clicked.connect(self.click_input)
        self.save_input_pushButton.clicked.connect(self.save_input)

        # 设置为只读
        self.input1_lineEdit.setReadOnly(True)
        self.input2_lineEdit.setReadOnly(True)
        self.input3_lineEdit.setReadOnly(True)

        # 安装事件过滤器
        self.input1_lineEdit.installEventFilter(self)
        self.input2_lineEdit.installEventFilter(self)
        self.input3_lineEdit.installEventFilter(self)

        self.parent = parent  # 保存父窗口引用

        if self.macro:
            self.macro_name_comboBox.setCurrentText(self.macro)
        if self.inputs:
            self.input_list_label.setText('原快捷键：' + self.inputs)

    def eventFilter(self, obj, event):
        """
        事件过滤器，用于捕获键盘按键事件。

        :param obj: 事件源对象。
        :param event: 事件对象。
        :return: 是否继续处理事件。
        """
        if event.type() == QtCore.QEvent.KeyPress:
            key = event.key()
            key_text = QtGui.QKeySequence(key).toString(QtGui.QKeySequence.NativeText)
            if key == QtCore.Qt.Key_Shift:
                key_text = 'Shift'
            elif key == QtCore.Qt.Key_Control:
                key_text = 'Ctrl'
            elif key == QtCore.Qt.Key_Alt:
                key_text = 'Alt'
            elif key == QtCore.Qt.Key_Meta:
                key_text = 'Windows'
            elif 'A' <= key_text <= 'Z':
                key_text = key_text.lower()
            if obj == self.input1_lineEdit:
                self.input1_lineEdit.setText(key_text)
            elif obj == self.input2_lineEdit:
                self.input2_lineEdit.setText(key_text)
            elif obj == self.input3_lineEdit:
                self.input3_lineEdit.setText(key_text)
            self.insert_input_line()
            return True
        return super(InputDialog, self).eventFilter(obj, event)

    def get_inputs(self):
        """
        获取当前输入的快捷键组合。
        """
        input1 = self.input1_lineEdit.text()
        input2 = self.input2_lineEdit.text()
        input3 = self.input3_lineEdit.text()
        inputs = [inp for inp in [input1, input2, input3] if inp is not None and inp != '']  # 过滤掉空的输入
        if inputs:
            input_list = '+'.join(inputs)
            self.inputs = input_list
        else:
            self.inputs = None

    def insert_input_line(self):
        """
        更新快捷键组合显示。
        """
        self.get_inputs()
        self.input_list_label.setText(self.inputs)

    def click_input(self):
        """
        处理启用复选框的点击事件。
        """
        self.enable = self.enable_checkBox.isChecked()  # 点下为True, 取消为False

    def delete_input_line(self):
        """
        清空快捷键输入框和显示。
        """
        self.inputs = None
        self.input1_lineEdit.clear()
        self.input2_lineEdit.clear()
        self.input3_lineEdit.clear()
        self.input_list_label.clear()

    def get_macro_name(self):
        """
        获取所有宏命令的名称。

        :return: 宏命令名称列表。
        """
        try:
            macro_data = utils.read_json(config.MACRO_FILE, {})
            if isinstance(macro_data, dict):
                return list(macro_data.keys())
        except Exception as e:
            self.info_label.setText(f"读取宏命令时出错: {str(e)}")
        return []

    def save_input(self):
        """
        保存快捷键组合并清空输入框。
        """
        self.submit()
        self.delete_input_line()

    def submit(self):
        """
        提交快捷键组合并保存到配置文件。
        """
        if not self.inputs:
            self.info_label.setText('未设置快捷键')
            return
        if not self.macro_name_comboBox.currentText():
            self.info_label.setText('无可用宏命令')
            return

        try:
            keys_data = utils.read_json(config.KEYS_FILE, {})
            if self.opened == 'insert':
                i = 1
                while f"快捷键_{i}" in keys_data:
                    i += 1
                self.name = f"快捷键_{i}"
            keys_data[self.name] = {
                "input_keys": self.inputs,
                "input_macro": self.macro_name_comboBox.currentText(),
                "input_enable": self.enable
            }
            utils.write_json(config.KEYS_FILE, keys_data)
            self.info_label.setText(f'{self.name} 保存成功')

            if self.parent:
                self.parent.load_keys()  # 调用父窗口的load_keys方法
        except Exception as e:
            self.info_label.setText(f"保存快捷键时出错: {str(e)}")

    def return_accept(self):
        """
        提交快捷键组合并关闭对话框。
        """
        self.submit()
        super().accept()  # 调用父类的accept方法
