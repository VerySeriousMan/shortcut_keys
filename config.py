# -*- coding: utf-8 -*-
"""
Project Name: Shortcut_keys
File Created: 2024.06.28
Author: ZhangYuetao
File Name: config.py
last renew 2024.06.28
"""

import os
import toml

# 定义默认参数值
DEFAULT_CONFIG = {
    'venv_path': None,
    'root_password': None,
    'server_ip': "10.0.1.206",
    'share_name': "public_intern",
    'username': "samba_intern",
    'password': "cnNa2Z"
}

CONFIG_FILE = r'settings/.secret.toml'


def load_config():
    # 尝试读取现有的 TOML 文件
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = toml.load(f)
        else:
            config = DEFAULT_CONFIG
    except (FileNotFoundError, toml.TomlDecodeError):
        config = DEFAULT_CONFIG

    # 检查是否缺少必要的参数，如果缺少则更新为默认值
    for key, value in DEFAULT_CONFIG.items():
        if key not in config:
            config[key] = value

    return config


def save_config(config):
    # 将更新后的配置写入 TOML 文件
    with open(CONFIG_FILE, 'w') as f:
        toml.dump(config, f)
