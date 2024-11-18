# -*- coding: utf-8 -*-
"""
Project Name: Shortcut_keys
File Created: 2024.06.24
Author: ZhangYuetao
File Name: main.py
last renew 2024.11.18
"""

import os.path
import subprocess
import time
import sys
import shutil
import platform

from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PyQt5 import QtGui, QtCore
import qt_material
import keyboard

from shortcut_keys import Ui_MainWindow
from macro_manage import MacroCommandWindow
from working_thread import WorkerThread
from keys_insert import InputDialog
from utils import read_json, write_json
from system_init import linux_init
import server_connect


if platform.system() == 'Linux':  # 检测用户操作系统
    linux_init()


class MyClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("快捷键宏命令软件V1.2")
        self.setWindowIcon(QtGui.QIcon("xey.ico"))

        self.current_key = None
        self.keys = {}
        self.delay_time = 0.1
        self.delay_doubleSpinBox.setValue(0.10)
        self.current_software_path = self.get_file_path()
        self.current_software_version = server_connect.get_current_software_version(self.current_software_path)
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
        self.change_key_pushButton.clicked.connect(self.change_key_combo_window)
        self.delete_key_pushButton.clicked.connect(self.delete_key)
        self.key_name_listWidget.itemClicked.connect(self.display_key_info)
        self.change_enable_pushButton.clicked.connect(self.change_key_enable)
        self.key_name_listWidget.itemDoubleClicked.connect(self.rename_key)
        self.software_update_action.triggered.connect(self.update_software)

        self.load_keys()
        self.auto_update()
        self.init_update()

    def init_update(self):
        dir_path = os.path.dirname(self.current_software_path)
        dir_name = os.path.basename(dir_path)
        if dir_name == 'temp':
            old_dir_path = os.path.dirname(dir_path)
            for file in os.listdir(old_dir_path):
                if file.endswith('.exe'):
                    old_software = os.path.join(old_dir_path, file)
                    os.remove(old_software)
            shutil.copy2(self.current_software_path, old_dir_path)
            new_file_path = os.path.join(old_dir_path, os.path.basename(self.current_software_path))
            if os.path.exists(new_file_path) and server_connect.is_file_complete(new_file_path):
                msg_box = QMessageBox(self)  # 创建一个新的 QMessageBox 对象
                reply = msg_box.question(self, '更新完成', '软件更新完成，需要立即重启吗？',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                msg_box.raise_()  # 确保弹窗显示在最上层

                if reply == QMessageBox.Yes:
                    subprocess.Popen(new_file_path)
                    time.sleep(1)
                    sys.exit("程序已退出")
                else:
                    sys.exit("程序已退出")
        else:
            is_updated = 0
            for file in os.listdir(dir_path):
                if file == 'temp':
                    is_updated = 1
                    shutil.rmtree(file)
            if is_updated == 1:
                try:
                    text = server_connect.get_update_log('快捷键宏命令软件')
                    QMessageBox.information(self, '更新成功', f'更新成功！\n{text}')
                except Exception as e:
                    QMessageBox.critical(self, '更新成功', f'日志加载失败: {str(e)}')

    @staticmethod
    def get_file_path():
        # 检查是否是打包后的程序
        if getattr(sys, 'frozen', False):
            # PyInstaller 打包后的路径
            current_path = os.path.abspath(sys.argv[0])
        else:
            # 非打包情况下的路径
            current_path = os.path.abspath(__file__)
        return current_path

    def auto_update(self):
        dir_path = os.path.dirname(self.current_software_path)
        dir_name = os.path.basename(dir_path)
        if dir_name != 'temp':
            if server_connect.check_version(self.current_software_version) == 1:
                self.update_software()

    def update_software(self):
        update_way = server_connect.check_version(self.current_software_version)
        if update_way == -1:
            # 网络未连接，弹出提示框
            QMessageBox.warning(self, '更新提示', '网络未连接，暂时无法更新')
        elif update_way == 0:
            # 当前已为最新版本，弹出提示框
            QMessageBox.information(self, '更新提示', '当前已为最新版本')
        else:
            # 弹出提示框，询问是否立即更新
            msg_box = QMessageBox(self)  # 创建一个新的 QMessageBox 对象
            reply = msg_box.question(self, '更新提示', '发现新版本，开始更新吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            msg_box.raise_()  # 确保弹窗显示在最上层

            if reply == QMessageBox.Yes:
                try:
                    server_connect.update_software(os.path.dirname(self.current_software_path), '快捷键宏命令软件')
                    text = server_connect.get_update_log('快捷键宏命令软件')
                    QMessageBox.information(self, '更新成功', f'更新成功！\n{text}')
                except Exception as e:
                    QMessageBox.critical(self, '更新失败', f'更新失败: {str(e)}')
            else:
                pass

    def submit(self):
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
        self.get_right_keys()
        self.key_name_listWidget.addItems(self.keys.keys())

    def change_key_enable(self):
        current_item = self.key_name_listWidget.currentItem()
        if current_item:
            key_name = current_item.text()
            if key_name in self.keys:
                self.keys[key_name]['input_enable'] = not self.keys[key_name]['input_enable']  # 切换 enable 状态
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

    def get_macro_name(self):
        try:
            macro_data = read_json(self.macro_json_path, {})
            if isinstance(macro_data, dict):
                return list(macro_data.keys())
        except Exception as e:
            self.error_label.setText(f"读取宏命令时出错: {str(e)}")
        return []

    def get_right_keys(self):
        macro_names = self.get_macro_name()
        keys_to_delete = []
        for key_name in self.keys.keys():
            if self.keys[key_name]['input_macro'] not in macro_names:
                keys_to_delete.append(key_name)

        for key_name in keys_to_delete:
            del self.keys[key_name]

        self.save_keys()

    def update_info_label(self, text):
        self.info_label.setText(text)

    def update_error_label(self, text):
        self.error_label.setText(text)

    def thread_finished(self):
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
        if self.worker_thread:
            self.worker_thread.stop()
            self.worker_thread.wait()  # 等待线程完全停止
            self.worker_thread = None  # 删除工作线程对象
        self.info_label.setText('程序已关闭')

    def open_macro_command_window(self):
        self.macro_command_window = MacroCommandWindow()
        self.macro_command_window.closed.connect(self.load_keys)  # 连接 closed 信号到 load_keys
        self.macro_command_window.show()

    def open_key_combo_window(self):
        if not self.is_key_combo_window_open:
            self.key_combo_window = InputDialog(parent=self, opened='insert')  # 传递父窗口引用
            self.key_combo_window.finished.connect(self.load_keys)
            self.key_combo_window.finished.connect(self.set_key_combo_window_closed)
            self.is_key_combo_window_open = True
            self.key_combo_window.show()

    def change_key_combo_window(self):
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
        self.is_key_combo_window_open = False

    def closeEvent(self, event):
        self.close_program()
        if self.macro_command_window:
            self.macro_command_window.close()
        event.accept()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.ApplicationActivate:
            # keyboard包bug，按下win+l锁屏后，只检测到win+l键按下，没检测到放开，所以系统恢复后先清楚残余按键表
            keyboard._pressed_events.clear()
        return super(MyClass, self).eventFilter(source, event)


if __name__ == "__main__":
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 自适应适配不同分辨率
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    myWin = MyClass()
    qt_material.apply_stylesheet(app, theme='default')
    app.installEventFilter(myWin)  # 添加事件过滤器捕获系统恢复
    myWin.show()
    sys.exit(app.exec_())
