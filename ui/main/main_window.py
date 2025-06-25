# -*- coding: utf-8 -*-
"""
Project Name: shortcut_keys
File Created: 2025.04.24
Author: ZhangYuetao
File Name: main_window.py
Update: 2025.06.25
"""

import platform

from PyQt5.QtWidgets import QMainWindow, QInputDialog, QMessageBox
from PyQt5 import QtGui, QtCore
import keyboard

import config
import utils
from ui.shortcut_keys import Ui_MainWindow
from ui.main.macro_manage import MacroCommandWindow
from ui.main.keys_insert import InputDialog
from ui.main.feedback_main import FeedbackWindow
from thread.work_thread import WorkerThread
from system_init import linux_init
from network.software_update import Updater
from network import server_connect

if platform.system() == 'Linux':  # 检测用户操作系统
    linux_init()


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    快捷键宏命令软件的主窗口类，用于管理和执行快捷键宏命令。

    Attributes:
        current_key (str): 当前选中的快捷键名称。
        keys (dict): 存储所有快捷键及其配置的字典。
        delay_time (float): 快捷键执行的延迟时间。
        current_software_path (str): 当前软件的路径。
        current_software_version (str): 当前软件的版本号。
        updater(Updater): 自动更新类。
        macro_command_window (MacroCommandWindow): 宏命令管理窗口。
        key_combo_window (InputDialog): 快捷键输入窗口。
        worker_thread (WorkerThread): 工作线程，用于执行快捷键宏命令。
        is_running (bool): 标志工作线程是否正在运行。
        feedback_window (FeedbackWindow): 问题反馈窗口对象。
        is_key_combo_window_open (bool): 标志快捷键输入窗口是否已打开。
    """

    def __init__(self, window_title, parent=None):
        """
        初始化主窗口，设置窗口图标、标题，并连接信号与槽。

        :param window_title: 窗口标题，由外部传入。
        :param parent: 父窗口对象，默认为 None。
        """
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(config.ICO_FILE))
        self.setWindowTitle(window_title)

        self.current_key = None
        self.keys = {}
        self.delay_time = 0.1
        self.current_software_path = utils.get_current_software_path()
        self.current_software_version = server_connect.get_current_software_version(self.current_software_path)
        
        self.updater = Updater(self.current_software_path, self.current_software_version)
        self.macro_command_window = None
        self.key_combo_window = None
        self.worker_thread = None  # 工作线程
        self.is_running = False  # 标志线程是否运行
        self.feedback_window = None
        self.is_key_combo_window_open = False  # 标志 InputDialog 是否已打开

        # 连接按钮信号与槽函数
        self.submit_pushButton.clicked.connect(self.submit)
        self.close_pushButton.clicked.connect(self.close_program)
        self.open_macro_command_pushButton.clicked.connect(self.open_macro_command_window)
        self.insert_input_pushButton.clicked.connect(self.open_key_combo_window)
        self.change_key_pushButton.clicked.connect(self.change_key_combo_window)
        self.delete_key_pushButton.clicked.connect(self.delete_key)
        self.key_name_listWidget.itemClicked.connect(self.display_key_info)
        self.change_enable_pushButton.clicked.connect(self.change_key_enable)
        self.key_name_listWidget.itemDoubleClicked.connect(self.rename_key)
        self.software_update_action.triggered.connect(self.updater.update_software)
        self.problem_feedback_action.triggered.connect(self.feedback_problem)

        self.updater.auto_update()
        self.updater.init_update()
        
        # 加载快捷键配置
        self.delay_doubleSpinBox.setValue(0.10)
        self.load_keys()

    def feedback_problem(self):
        """
        处理问题反馈操作，检查网络连接并打开反馈窗口。
        """
        if server_connect.check_version(self.current_software_version) == -1:
            QMessageBox.warning(self, '网络未连接', '网络未连接，请连接内网后再试')
        else:
            self.open_feedback_window()

    def submit(self):
        """
        提交任务，启动工作线程执行快捷键宏命令。
        """
        if self.keys != {} and not self.is_running:
            self.error_label.clear()
            self.delay_time = self.delay_doubleSpinBox.text()
            self.worker_thread = WorkerThread(self.keys, self.delay_time)
            self.worker_thread.update_info_label.connect(self.update_info_label)
            self.worker_thread.update_error_label.connect(self.update_error_label)
            self.worker_thread.thread_finished.connect(self.thread_finished)  # 连接线程结束信号
            self.worker_thread.start()
            self.is_running = True  # 设置标志，表示线程已启动
            # 禁用按钮
            self.submit_pushButton.setEnabled(False)
            self.insert_input_pushButton.setEnabled(False)
            self.delete_key_pushButton.setEnabled(False)
            self.change_enable_pushButton.setEnabled(False)
            self.open_macro_command_pushButton.setEnabled(False)
            self.delay_doubleSpinBox.setEnabled(False)
            self.change_key_pushButton.setEnabled(False)
            # 关闭子界面
            if self.macro_command_window:
                self.macro_command_window.close()
            if self.key_combo_window:
                self.key_combo_window.close()
        else:
            self.info_label.setText('快捷键为空')

    def delete_key(self):
        """
        删除当前选中的快捷键。
        """
        current_key = self.key_name_listWidget.currentItem()
        if current_key:
            key_name = current_key.text()
            del self.keys[key_name]
            self.key_name_listWidget.takeItem(self.key_name_listWidget.row(current_key))
            self.key_info_listWidget.clear()
            self.current_key = None
            self.save_keys()
            self.error_label.clear()

    def save_keys(self):
        """
        保存快捷键配置到 JSON 文件。
        """
        utils.write_json(config.KEYS_FILE, self.keys)

    def load_keys(self):
        """
        从 JSON 文件加载快捷键配置并更新界面。
        """
        self.key_name_listWidget.clear()
        self.key_info_listWidget.clear()
        self.keys = utils.read_json(config.KEYS_FILE, {})
        self.get_right_keys()
        self.key_name_listWidget.addItems(self.keys.keys())

    def change_key_enable(self):
        """
        切换当前选中快捷键的启用状态。
        """
        current_item = self.key_name_listWidget.currentItem()
        if current_item:
            key_name = current_item.text()
            if key_name in self.keys:
                self.keys[key_name]['input_enable'] = not self.keys[key_name]['input_enable']  # 切换 enable 状态
                self.save_keys()
                self.display_key_info(current_item)
                self.error_label.clear()

    def display_key_info(self, item):
        """
        显示当前选中快捷键的详细信息。

        :param item: 当前选中的快捷键项。
        """
        key_name = item.text()
        self.current_key = key_name
        self.key_info_listWidget.clear()
        if key_name in self.keys:
            key_info = self.keys[key_name]
            input_keys = key_info.get("input_keys", "")
            input_macro = key_info.get("input_macro", "")
            input_enable = key_info.get("input_enable", "")

            self.key_info_listWidget.addItem(f"输入的快捷键: {input_keys}")
            self.key_info_listWidget.addItem(f"输出的宏命令: {input_macro}")
            self.key_info_listWidget.addItem(f"启用状态: {input_enable}")
        self.key_info_listWidget.repaint()  # 刷新列表显示

    def rename_key(self, item):
        """
        重命名当前选中的快捷键。

        :param item: 当前选中的快捷键项。
        """
        old_name = item.text()
        new_name, ok = QInputDialog.getText(self, "快捷键重命名", "新快捷键名称:", text=old_name)
        if ok and new_name:
            self.keys[new_name] = self.keys.pop(old_name)
            item.setText(new_name)
            self.save_keys()
            if self.current_key == old_name:
                self.current_key = new_name

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
            self.error_label.setText(f"读取宏命令时出错: {str(e)}")
        return []

    def get_right_keys(self):
        """
        检查并删除无效的快捷键配置。
        """
        macro_names = self.get_macro_name()
        keys_to_delete = []
        for key_name in self.keys.keys():
            if self.keys[key_name]['input_macro'] not in macro_names:
                keys_to_delete.append(key_name)

        for key_name in keys_to_delete:
            del self.keys[key_name]

        self.save_keys()

    def update_info_label(self, text):
        """
        更新信息标签的文本。

        :param text: 要显示的文本。
        """
        self.info_label.setText(text)

    def update_error_label(self, text):
        """
        更新错误标签的文本。

        :param text: 要显示的文本。
        """
        self.error_label.setText(text)

    def thread_finished(self):
        """
        处理工作线程完成后的操作。
        """
        self.is_running = False  # 重置标志
        self.worker_thread = None
        # 启用按钮
        self.submit_pushButton.setEnabled(True)
        self.insert_input_pushButton.setEnabled(True)
        self.delete_key_pushButton.setEnabled(True)
        self.change_enable_pushButton.setEnabled(True)
        self.open_macro_command_pushButton.setEnabled(True)
        self.delay_doubleSpinBox.setEnabled(True)
        self.change_key_pushButton.setEnabled(True)

    def close_program(self):
        """
        关闭程序，停止工作线程。
        """
        if self.worker_thread:
            self.worker_thread.stop()
            self.worker_thread.wait()  # 等待线程完全停止
            self.worker_thread = None  # 删除工作线程对象
        self.info_label.setText('程序已关闭')

    def open_feedback_window(self):
        """
        打开问题反馈窗口。
        """
        self.feedback_window = FeedbackWindow()
        self.feedback_window.show()

    def open_macro_command_window(self):
        """
        打开宏命令管理窗口。
        """
        self.macro_command_window = MacroCommandWindow()
        self.macro_command_window.closed.connect(self.load_keys)  # 连接 closed 信号到 load_keys
        self.macro_command_window.show()

    def open_key_combo_window(self):
        """
        打开快捷键输入窗口。
        """
        if not self.is_key_combo_window_open:
            self.key_combo_window = InputDialog(parent=self, opened='insert')  # 传递父窗口引用
            self.key_combo_window.finished.connect(self.load_keys)
            self.key_combo_window.finished.connect(self.set_key_combo_window_closed)
            self.is_key_combo_window_open = True
            self.key_combo_window.show()

    def change_key_combo_window(self):
        """
        打开快捷键修改窗口。
        """
        if not self.is_key_combo_window_open:
            current_item = self.key_name_listWidget.currentItem()
            if current_item:
                key_name = current_item.text()
                inputs = self.keys[key_name].get("input_keys", "")
                macro = self.keys[key_name].get("input_macro", "")
                enable = self.keys[key_name].get("input_enable", "")
                self.key_combo_window = InputDialog(parent=self, name=key_name, inputs=inputs, macro=macro, enable=enable, opened='change')
                self.key_combo_window.finished.connect(self.load_keys)
                self.key_combo_window.finished.connect(self.set_key_combo_window_closed)
                self.is_key_combo_window_open = True
                self.key_combo_window.show()

    def set_key_combo_window_closed(self):
        """
        设置快捷键输入窗口关闭标志。
        """
        self.is_key_combo_window_open = False

    def closeEvent(self, event):
        """
        处理窗口关闭事件，停止工作线程并关闭子窗口。

        :param event: 关闭事件。
        """
        self.close_program()
        if self.macro_command_window:
            self.macro_command_window.close()
        if self.feedback_window:
            self.feedback_window.close()
        event.accept()

    def eventFilter(self, source, event):
        """
        事件过滤器，用于捕获系统恢复事件。

        :param source: 事件源。
        :param event: 事件对象。
        :return: 是否继续处理事件。
        """
        if event.type() == QtCore.QEvent.ApplicationActivate:
            # keyboard包bug，按下win+l锁屏后，只检测到win+l键按下，没检测到放开，所以系统恢复后先清楚残余按键表
            keyboard._pressed_events.clear()
        return super(MainWindow, self).eventFilter(source, event)
