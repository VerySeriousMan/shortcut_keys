# -*- coding: utf-8 -*-
"""
Project Name: shortcut_keys
File Created: 2024.06.26
Author: ZhangYuetao
File Name: macro_manage.py
Update: 2025.06.25
"""

from PyQt5.QtWidgets import QWidget, QInputDialog
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

import config
from ui.macro_command import Ui_Form
from utils import read_json, write_json


class MacroCommandWindow(QWidget, Ui_Form):
    """
    宏命令管理窗口类，用于管理和编辑宏命令。

    Attributes:
        closed (pyqtSignal): 窗口关闭时发出的信号。
        output_list (list): 当前宏命令的输出操作列表。
        macros (dict): 存储所有宏命令及其操作的字典。
        current_macro (str): 当前选中的宏命令名称。
    """

    closed = pyqtSignal()  # 定义关闭信号

    def __init__(self, parent=None):
        """
        初始化宏命令管理窗口。

        :param parent: 父窗口对象，默认为 None。
        """
        super(MacroCommandWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("宏命令管理")
        self.setWindowIcon(QtGui.QIcon(config.ICO_FILE))
        
        self.output_list = []
        self.macros = {}  # 存储宏命令及其操作
        self.current_macro = None

        # 连接按钮信号与槽函数
        self.insert_output_keyboard_pushButton.clicked.connect(self.insert_output_line)
        self.insert_output_mouse_pushButton.clicked.connect(self.insert_output_box)
        self.cut_output_pushButton.clicked.connect(self.cut_output_line)
        self.time_pushButton.clicked.connect(self.insert_output_time)
        self.delete_output_pushButton.clicked.connect(self.delete_output_line)
        self.delete_all_outputs_pushButton.clicked.connect(self.delete_all_outputs)
        self.new_macro_pushButton.clicked.connect(self.new_macro)
        self.delete_macro_pushButton.clicked.connect(self.delete_macro)
        self.up_pushButton.clicked.connect(self.move_up)
        self.down_pushButton.clicked.connect(self.move_down)
        self.return_pushButton.clicked.connect(self.return_main_window)
        self.macro_list_listWidget.itemClicked.connect(self.display_macro_operations)
        self.macro_list_listWidget.itemDoubleClicked.connect(self.rename_macro)

        # 设置为只读
        self.output_lineEdit.setReadOnly(True)
        # 安装事件过滤器
        self.output_lineEdit.installEventFilter(self)
        self.mouse_comboBox.addItems(['click_right', 'click_left', 'click_middle',
                                      'double_click', 'scroll_up', 'scroll_down'])

        self.load_macros()  # 启动时加载宏命令json文件

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
            if obj == self.output_lineEdit:
                self.output_lineEdit.setText(key_text)
            return True
        return super(MacroCommandWindow, self).eventFilter(obj, event)

    def insert_output_line(self):
        """
        将当前输入框中的内容插入到宏命令操作列表中。
        """
        if self.current_macro:
            new_output = self.output_lineEdit.text()
            if new_output:
                self.macros[self.current_macro].append(new_output)
                self.macro_command_listWidget.addItem(new_output)
                self.output_lineEdit.clear()
                self.save_macros()

    def insert_output_box(self):
        """
        将当前鼠标操作插入到宏命令操作列表中。
        """
        if self.current_macro:
            new_output = self.mouse_comboBox.currentText()
            if new_output:
                self.macros[self.current_macro].append('---')
                self.macro_command_listWidget.addItem('---')
                self.macros[self.current_macro].append(new_output)
                self.macro_command_listWidget.addItem(new_output)
                self.macros[self.current_macro].append('---')
                self.macro_command_listWidget.addItem('---')
                self.save_macros()

    def cut_output_line(self):
        """
        在宏命令操作列表中插入分隔线。
        """
        if self.current_macro:
            self.macros[self.current_macro].append('---')
            self.macro_command_listWidget.addItem('---')
            self.save_macros()

    def insert_output_time(self):
        """
        在宏命令操作列表中插入时间间隔。
        """
        if self.current_macro:
            add_time = 'time_' + self.time_doubleSpinBox.text()
            self.macro_command_listWidget.addItem('---')
            self.macros[self.current_macro].append('---')
            self.macros[self.current_macro].append(add_time)
            self.macro_command_listWidget.addItem(add_time)
            self.macro_command_listWidget.addItem('---')
            self.macros[self.current_macro].append('---')

    def delete_output_line(self):
        """
        删除当前选中的宏命令操作。
        """
        current_item = self.macro_command_listWidget.currentItem()
        if current_item:
            self.macros[self.current_macro].remove(current_item.text())
            self.macro_command_listWidget.takeItem(self.macro_command_listWidget.row(current_item))
            self.save_macros()

    def delete_all_outputs(self):
        """
        删除当前宏命令的所有操作。
        """
        if self.current_macro:
            self.macros[self.current_macro] = []
            self.macro_command_listWidget.clear()
            self.save_macros()

    def new_macro(self):
        """
        创建新的宏命令。
        """
        macro_index = 1
        while f"宏命令_{macro_index}" in self.macros:
            macro_index += 1
        new_macro_name = f"宏命令_{macro_index}"
        self.macros[new_macro_name] = []
        self.macro_list_listWidget.addItem(new_macro_name)
        self.save_macros()

    def delete_macro(self):
        """
        删除当前选中的宏命令。
        """
        current_item = self.macro_list_listWidget.currentItem()
        if current_item:
            macro_name = current_item.text()
            del self.macros[macro_name]
            self.macro_list_listWidget.takeItem(self.macro_list_listWidget.row(current_item))
            self.macro_command_listWidget.clear()
            self.current_macro = None
            self.save_macros()

    def display_macro_operations(self, item):
        """
        显示当前选中宏命令的操作列表。

        :param item: 当前选中的宏命令项。
        """
        macro_name = item.text()
        self.current_macro = macro_name
        self.macro_command_listWidget.clear()
        self.macro_command_listWidget.addItems(self.macros[macro_name])
        self.macro_command_listWidget.repaint()  # 刷新列表显示

    def move_up(self):
        """
        将当前选中的宏命令操作向上移动。
        """
        current_row = self.macro_command_listWidget.currentRow()
        if current_row > 0:
            current_item = self.macro_command_listWidget.takeItem(current_row)
            self.macro_command_listWidget.insertItem(current_row - 1, current_item)
            self.macro_command_listWidget.setCurrentRow(current_row - 1)
            self.macros[self.current_macro].insert(current_row - 1, self.macros[self.current_macro].pop(current_row))
            self.save_macros()

    def move_down(self):
        """
        将当前选中的宏命令操作向下移动。
        """
        current_row = self.macro_command_listWidget.currentRow()
        if current_row < self.macro_command_listWidget.count() - 1:
            current_item = self.macro_command_listWidget.takeItem(current_row)
            self.macro_command_listWidget.insertItem(current_row + 1, current_item)
            self.macro_command_listWidget.setCurrentRow(current_row + 1)
            self.macros[self.current_macro].insert(current_row + 1, self.macros[self.current_macro].pop(current_row))
            self.save_macros()

    def return_main_window(self):
        """
        关闭宏命令管理窗口。
        """
        self.close()

    def rename_macro(self, item):
        """
        重命名当前选中的宏命令。

        :param item: 当前选中的宏命令项。
        """
        old_name = item.text()
        new_name, ok = QInputDialog.getText(self, "宏命令重命名", "新宏命令名称:", text=old_name)
        if ok and new_name:
            self.macros[new_name] = self.macros.pop(old_name)
            item.setText(new_name)
            self.save_macros()
            if self.current_macro == old_name:
                self.current_macro = new_name

    def save_macros(self):
        """
        保存宏命令配置到 JSON 文件。
        """
        write_json(config.MACRO_FILE, self.macros)

    def load_macros(self):
        """
        从 JSON 文件加载宏命令配置并更新界面。
        """
        self.macros = read_json(config.MACRO_FILE, {})
        self.macro_list_listWidget.addItems(self.macros.keys())

    def closeEvent(self, event):
        """
        处理窗口关闭事件，发出关闭信号。

        :param event: 关闭事件。
        """
        self.closed.emit()  # 关闭窗口时发出信号
        super(MacroCommandWindow, self).closeEvent(event)
