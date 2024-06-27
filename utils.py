# -*- coding: utf-8 -*-
"""
Project Name: Shortcut_keys
File Created: 2024.06.27
Author: ZhangYuetao
File Name: utils.py
last renew 2024.06.27
"""

import os
import json


def read_json(file_path, default_value):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                return json.load(file)
        except json.JSONDecodeError:
            pass
    return default_value


def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8', errors='ignore') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
