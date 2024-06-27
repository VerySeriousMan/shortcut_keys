# -*- coding: utf-8 -*-
"""
Project Name: Shortcut_keys
File Created: 2024.06.26
Author: ZhangYuetao
File Name: working_thread.py
last renew 2024.06.27
"""

import time

import keyboard
import pyautogui
from PyQt5.QtCore import QThread, pyqtSignal
from utils import read_json


class WorkerThread(QThread):
    update_info_label = pyqtSignal(str)
    update_error_label = pyqtSignal(str)
    thread_finished = pyqtSignal()  # 用于线程结束时通知主线程

    def __init__(self, keys):
        super(WorkerThread, self).__init__()
        self.keys = keys
        self.doing_done = False
        self.running = True
        self.macros_path = r'settings/macros.json'  # 宏命令json文件路径

    def run(self):
        try:
            if self.keys != {}:
                for key_name in self.keys.keys():
                    key = self.keys[key_name]
                    if key['input_enable'] is True:
                        keyboard.add_hotkey(key['input_keys'], self.key_action(key['input_macro']))
                        # print(f"input_keys=={key['input_keys']}-------input_macro=={key['input_macro']}")
                self.update_info_label.emit('程序运行中')

                while self.running:
                    time.sleep(0.1)
                keyboard.unhook_all()  # 确保在退出前取消所有快捷键绑定
            else:
                self.update_info_label.emit('存在空值')
        except Exception as e:
            self.update_error_label.emit(f"错误: {str(e)}")
        finally:
            self.thread_finished.emit()  # 通知主线程，线程已结束

    def key_action(self, macro):
        def action():
            try:
                macros = read_json(self.macros_path, {})
                # print(f"macros=={macros}")
                output_list = []
                if macro in macros.keys():
                    for line in macros[macro]:
                        output_list.append(line)
                # print(f"output_list=={output_list}")

                outputs = '+'.join(output_list)
                outputs = outputs.replace('+---', '---').replace('---+', '---')
                # print(f"outputs=={outputs}")

                if not self.doing_done and outputs:
                    self.doing_done = True
                    output_things = outputs.split('---')
                    for output_thing in output_things:
                        try:
                            if output_thing:
                                # print(f"output_thing=={output_thing}")
                                if output_thing.startswith("click"):
                                    button = output_thing.split('_')[1] if '_' in output_thing else 'left'
                                    pyautogui.click(button=button)
                                elif output_thing == 'double_click':
                                    pyautogui.doubleClick()
                                elif output_thing.startswith("move"):
                                    try:
                                        _, x, y = output_thing.split('_')
                                        pyautogui.moveTo(int(x), int(y))
                                    except ValueError:
                                        self.update_error_label.emit(f"错误的鼠标移动命令: {output_thing}")
                                else:
                                    keyboard.press_and_release(output_thing)
                        except Exception as e:
                            self.update_error_label.emit(f"错误的命令: {output_thing} ({str(e)})")
                    time.sleep(0.1)  # 避免快速重复触发
                    self.doing_done = False
            except Exception as e:
                self.update_error_label.emit(f"执行宏命令时出错: {str(e)}")

        return action

    def stop(self):
        self.running = False
        keyboard.unhook_all()
