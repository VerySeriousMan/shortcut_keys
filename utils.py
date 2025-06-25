# -*- coding: utf-8 -*-
"""
Project Name: shortcut_keys
File Created: 2024.06.27
Author: ZhangYuetao
File Name: utils.py
Update: 2025.06.25
"""

import os
import json
import sys


def read_json(file_path, default_value):
    """
    读取json文件。

    :param file_path: json文件地址。
    :param default_value: 默认参数。
    :return: 若正确打开文件，返回json信息，若文件不存在或打开失败，则返回默认参数。
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                return json.load(file)
        except json.JSONDecodeError:
            pass
    return default_value


def write_json(file_path, data):
    """
    将数据写入json文件。

    :param file_path: 保存地址。
    :param data: 要写入的数据。
    """
    with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_current_software_path():
    """
    获取当前软件的可执行文件路径。

    :return: 当前软件的可执行文件路径。
    """
    # 检查是否是打包后的程序
    if getattr(sys, 'frozen', False):
        # PyInstaller 打包后的路径
        return os.path.abspath(sys.argv[0])
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'main.py')
