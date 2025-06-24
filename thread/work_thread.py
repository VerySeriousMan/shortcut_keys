# -*- coding: utf-8 -*-
"""
Project Name: shortcut_keys
File Created: 2024.06.26
Author: ZhangYuetao
File Name: work_thread.py
Update: 2025.05.13
"""

import time

import keyboard
import pyautogui

from PyQt5.QtCore import QThread, pyqtSignal
from utils import read_json
import config


class WorkerThread(QThread):
    """
    工作线程类，用于在后台监听快捷键并执行对应的宏命令。

    Attributes:
        update_info_label (pyqtSignal): 更新状态信息的信号
        update_error_label (pyqtSignal): 更新错误信息的信号
        thread_finished (pyqtSignal): 线程结束通知信号
    """
    update_info_label = pyqtSignal(str)
    update_error_label = pyqtSignal(str)
    thread_finished = pyqtSignal()  # 用于线程结束时通知主线程

    def __init__(self, keys, delay_time):
        """
        初始化工作线程。

        :param keys: 包含快捷键配置的字典。
        :param delay_time: 命令执行后的延迟时间（秒）。
        """
        super(WorkerThread, self).__init__()
        self.keys = keys
        self.delay_time = float(delay_time)
        self.doing_done = False
        self.running = True
        self.pressed_lock = 0

        keyboard.on_press(self.on_lock_press)

    def on_lock_press(self, event):
        """
        win+l锁屏键按下时的回调函数，keyboard包bug，按下win+l锁屏后，只检测到win+l键按下，没检测到放开，所以锁屏后需清楚残余按键表。
        """
        if self.pressed_lock == 2:
            keyboard._pressed_events.clear()
            self.pressed_lock = 0

        if 'windows' in event.name:
            self.pressed_lock = 1
        elif (event.name == 'l' or event.name == 'L') and self.pressed_lock == 1:
            self.pressed_lock = 2

    def run(self):
        """
        线程主运行方法，注册所有启用的快捷键并保持线程运行。
        """
        try:
            if self.keys != {}:
                for key_name in self.keys.keys():
                    key = self.keys[key_name]
                    if key['input_enable'] is True:
                        keyboard.add_hotkey(key['input_keys'], self.key_action(key['input_macro']), suppress=True)
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
        """
        生成宏命令执行的回调函数。

        :param macro: 宏命令名称
        :return: 执行指定宏命令的回调函数
        """
        def action():
            """
            实际的宏命令执行逻辑，处理鼠标/键盘操作和时间间隔。
            """
            try:
                macros = read_json(config.MACRO_FILE, {})
                output_list = []
                if macro in macros.keys():
                    for line in macros[macro]:
                        output_list.append(line)

                outputs = '+'.join(output_list)
                outputs = outputs.replace('+---', '---').replace('---+', '---')

                if not self.doing_done and outputs:
                    self.doing_done = True
                    output_things = outputs.split('---')
                    for output_thing in output_things:
                        try:
                            if output_thing:
                                if output_thing.startswith("click"):
                                    button = output_thing.split('_')[1] if '_' in output_thing else 'left'
                                    pyautogui.click(button=button)
                                elif output_thing == 'double_click':
                                    pyautogui.doubleClick()
                                elif output_thing == 'scroll_up':
                                    pyautogui.scroll(50)
                                elif output_thing == 'scroll_down':
                                    pyautogui.scroll(-50)
                                elif output_thing.startswith("move"):
                                    try:
                                        _, x, y = output_thing.split('_')
                                        pyautogui.moveTo(int(x), int(y))
                                    except ValueError:
                                        self.update_error_label.emit(f"错误的鼠标移动命令: {output_thing}")
                                elif output_thing.startswith("time"):
                                    use_time = output_thing.split('_')[1]
                                    time.sleep(float(use_time))
                                else:
                                    if "windows" in output_thing.lower():
                                        self.pressed_win = True
                                    keyboard.press_and_release(output_thing)
                        except Exception as e:
                            self.update_error_label.emit(f"错误的命令: {output_thing} ({str(e)})")
                    time.sleep(self.delay_time)  # 避免快速重复触发
                    self.doing_done = False
            except Exception as e:
                self.update_error_label.emit(f"执行宏命令时出错: {str(e)}")

        return action

    def stop(self):
        """
        停止线程运行，取消所有快捷键注册。
        """
        self.running = False
        keyboard.unhook_all()
