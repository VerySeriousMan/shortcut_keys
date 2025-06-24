# -*- coding: utf-8 -*-
"""
Project Name: shortcut_keys
File Created: 2024.06.28
Author: ZhangYuetao
File Name: config.py
Update: 2025.06.24
"""

import os
import toml

# 定义默认参数值
LINUX_DEFAULT_CONFIG = {
    'venv_path': None,
    'root_password': None,
}

SECRET_FILE = r'settings/.secret.toml'
LINUX_CONFIG_FILE = r'settings/.linux.toml'
SOFTWARE_INFOS_FILE = r'settings/software_infos.toml'

ICO_FILE = r'settings/xey.ico'

MACRO_FILE = r'settings/macros.json'  # 宏命令json文件路径
KEYS_FILE = r'settings/keys.json'  # 快捷键json文件路径

SOFTWARE_NAME = "快捷键宏命令软件"
SHARE_DIR = r""  # 你的服务器上的软件文件夹地址
PROBLEM_SHARE_DIR = r""  # 你的服务器上的问题反馈文件夹地址


def load_config(filepath, default):
    """
    加载配置文件，如果文件不存在或解析失败则使用默认配置

    :param filepath: TOML 文件路径
    :param default: 默认配置字典
    :return: 加载的配置字典
    """
    # 尝试读取现有的 TOML 文件
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                config = toml.load(f)
        else:
            config = default
    except (FileNotFoundError, toml.TomlDecodeError):
        config = default

    # 检查是否缺少必要的参数，如果缺少则更新为默认值
    for key, value in default.items():
        if key not in config:
            config[key] = value

    return config


def load_credentials(config_path=SECRET_FILE):
    """
    从配置文件中加载服务器连接凭证。

    :param config_path: 配置文件的路径。
    :return: 包含服务器IP、共享名称、用户名和密码的元组。
    """
    with open(config_path, 'r') as config_file:
        config_info = toml.load(config_file)
        credentials = config_info.get("credentials", {})
        return (
            credentials.get("server_ip"),
            credentials.get("share_name"),
            credentials.get("username"),
            credentials.get("password"),
        )
