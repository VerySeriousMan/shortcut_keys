# -*- coding: utf-8 -*-
"""
Project Name: Shortcut_keys
File Created: 2024.06.24
Author: ZhangYuetao
File Name: main.py
last renew 2024.06.28
"""

import os
import sys
import platform
import subprocess

from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt5 import QtGui
import qt_material

import config
from shortcut_keys import Ui_MainWindow
from macro_manage import MacroCommandWindow
from working_thread import WorkerThread
from keys_insert import InputDialog
from utils import read_json, write_json

config_data = config.load_config()

venv_path = config_data['venv_path']
root_password = config_data['root_password']
is_linux = platform.system() == 'Linux'  # 检测用户操作系统
sys.path.append(os.path.join(venv_path, 'lib', 'python3.10', 'site-packages'))

if is_linux:
    # 检查是否是以 root 身份运行
    if os.geteuid() != 0:
        # 如果不是 root，则重新运行脚本并以 root 用户身份执行
        print("Switching to root user...")
        command = f'echo {root_password} | sudo -S {sys.executable} ' + ' '.join(sys.argv)
        subprocess.call(command, shell=True)
        sys.exit()

    # 激活虚拟环境
    activate_script = os.path.join(venv_path, 'bin', 'activate_this.py')
    if os.path.exists(activate_script):
        exec(open(activate_script).read(), {'__file__': activate_script})
        # 给root用户赋予图形界面操作权限
        xhost_command = 'xhost +SI:localuser:root'
        subprocess.run(xhost_command, shell=True, check=True)
    else:
        print(f"Could not find the virtual environment activation script at {activate_script}")
        sys.exit(1)


class MyClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("快捷键宏命令软件V1.0")
        self.setWindowIcon(QtGui.QIcon("xey.ico"))

        self.current_key = None
        self.keys = {}
        self.macro_json_path = r'settings/macros.json'  # 宏命令json文件路径
        self.keys_json_path = r'settings/keys.json'  # 快捷键json文件路径
        self.macro_command_window = None
        self.key_combo_window = None
        self.is_key_combo_window_open = False  # 标志 InputDialog 是否已打开

        self.worker_thread = None  # 工作线程
        self.is_running = False  # 标志线程是否运行

        self.submit_pushButton.clicked.connect(self.submit)
        self.close_pushButton.clicked.connect(self.close_program)
        self.open_macro_command_pushButton.clicked.connect(self.open_macro_command_window)
        self.insert_input_pushButton.clicked.connect(self.open_key_combo_window)
        self.delete_key_pushButton.clicked.connect(self.delete_key)
        self.key_name_listWidget.itemClicked.connect(self.display_key_info)
        self.change_enable_pushButton.clicked.connect(self.change_key_enable)
        self.key_name_listWidget.itemDoubleClicked.connect(self.rename_key)

        self.load_keys()

    def submit(self):
        if self.keys != {} and not self.is_running:
            self.error_label.clear()
            self.worker_thread = WorkerThread(self.keys)
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
        else:
            self.info_label.setText('快捷键为空')

    def delete_key(self):
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
        write_json(self.keys_json_path, self.keys)

    def load_keys(self):
        self.key_name_listWidget.clear()
        self.key_info_listWidget.clear()
        self.keys = read_json(self.keys_json_path, {})
        self.key_name_listWidget.addItems(self.keys.keys())

    def change_key_enable(self):
        current_item = self.key_name_listWidget.currentItem()
        if current_item:
            key_name = current_item.text()
            if key_name in self.keys:
                # 切换 enable 状态
                self.keys[key_name]['input_enable'] = not self.keys[key_name]['input_enable']
                self.save_keys()
                self.display_key_info(current_item)
                self.error_label.clear()

    def display_key_info(self, item):
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
        old_name = item.text()
        new_name, ok = QInputDialog.getText(self, "快捷键重命名", "新快捷键名称:", text=old_name)
        if ok and new_name:
            self.keys[new_name] = self.keys.pop(old_name)
            item.setText(new_name)
            self.save_keys()
            if self.current_key == old_name:
                self.current_key = new_name

    def update_info_label(self, text):
        self.info_label.setText(text)

    def update_error_label(self, text):
        self.error_label.setText(text)

    def thread_finished(self):
        self.is_running = False  # 重置标志
        # 启用按钮
        self.submit_pushButton.setEnabled(True)
        self.insert_input_pushButton.setEnabled(True)
        self.delete_key_pushButton.setEnabled(True)
        self.change_enable_pushButton.setEnabled(True)
        self.open_macro_command_pushButton.setEnabled(True)

    def close_program(self):
        if self.worker_thread:
            self.worker_thread.stop()
            self.worker_thread.wait()  # 等待线程完全停止
        if self.macro_command_window:
            self.macro_command_window.close()
        self.info_label.setText('程序已关闭')

    def open_macro_command_window(self):
        self.macro_command_window = MacroCommandWindow()
        self.macro_command_window.show()

    def open_key_combo_window(self):
        if not self.is_key_combo_window_open:
            self.key_combo_window = InputDialog(parent=self)  # 传递父窗口引用
            self.key_combo_window.finished.connect(self.load_keys)
            self.key_combo_window.finished.connect(self.set_key_combo_window_closed)
            self.is_key_combo_window_open = True
            self.key_combo_window.show()

    def set_key_combo_window_closed(self):
        self.is_key_combo_window_open = False

    def closeEvent(self, event):
        self.close_program()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyClass()
    qt_material.apply_stylesheet(app, theme='default')
    myWin.show()
    sys.exit(app.exec_())
