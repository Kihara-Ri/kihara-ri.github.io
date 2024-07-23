#!/usr/bin/python3

import os
import subprocess
from time import sleep

# define colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def start_mkdocs():
    # 指定端口
    cmd = "nohup mkdocs serve -a 0.0.0.0:32648 &"
    os.system(cmd)

    # 检查 mkdocs 服务状态
    status_cmd = "ps aux | grep 'mkdocs serve' | grep -v grep"
    result = subprocess.run(status_cmd, shell = True, capture_output = True, text = True)

    if result.stdout:
        print(f"Mkdocs 服务{GREEN}已启动{RESET}")
        print(f"服务状态: {GREEN}运行中{RESET}，运行端口为: 32648")
    else:
        print(f"Mkdocs 服务启动{RED}失败{RESET}")
        print(f"服务状态: {RED}未运行{RESET}")

if __name__ == "__main__":
    start_mkdocs()


