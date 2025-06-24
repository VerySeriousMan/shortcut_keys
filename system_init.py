# -*- coding: utf-8 -*-
"""
Project Name: shortcut_keys
File Created: 2024.07.05
Author: ZhangYuetao
File Name: system_init.py
Update: 2025.06.24
"""

import os
import sys
import subprocess

import config


def linux_init():
    """
    若为Linux系统，进行初始化配置与权限设置。
    """
    config_data = config.load_config(config.LINUX_CONFIG_FILE, config.LINUX_DEFAULT_CONFIG)

    venv_path = config_data['venv_path']
    root_password = config_data['root_password']

    sys.path.append(os.path.join(venv_path, 'lib', 'python3.10', 'site-packages'))

    # 检查是否是以 root 身份运行并且是否已经重新运行过
    if os.geteuid() != 0 and 'IS_RELAUNCHED' not in os.environ:
        # 如果不是 root，并且没有重新运行过，则重新运行脚本并以 root 用户身份执行
        print("Switching to root user...")
        os.environ['IS_RELAUNCHED'] = '1'
        command = f'echo {root_password} | sudo -S env IS_RELAUNCHED=1 {sys.executable} ' + ' '.join(sys.argv)
        subprocess.call(command, shell=True)
        sys.exit(0)  # 退出当前进程，避免继续执行后续代码

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
