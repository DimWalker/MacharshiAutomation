import threading
import time

import win32api
import win32con

from flowstep.flow_step import battle_simulation
from flowstep.game_window import active_game

import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志级别
    format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志格式
    datefmt='%Y-%m-%d %H:%M:%S'  # 设置时间格式
)

# # 输出不同级别的日志
# logging.debug("这是一个调试信息")
# logging.info("这是一个普通信息")
# logging.warning("这是一个警告信息")
# logging.error("这是一个错误信息")
# logging.critical("这是一个严重错误信息")


running = True


def stop_program():
    global running
    running = False
    print("程序即将停止...")


def thread_execute():
    # 战斗循环20次，手动修改
    battle_simulation(20)
    stop_program()


if __name__ == '__main__':
    active_game()
    # 等待窗口激活
    time.sleep(1)

    # 创建后台线程
    t = threading.Thread(target=thread_execute, daemon=True)
    t.start()

    print("程序正在运行，按 Ctrl+Shift+S 停止...")
    while running:
        # 检查Ctrl、Shift和S键是否同时按下
        if (win32api.GetAsyncKeyState(win32con.VK_CONTROL) < 0 and
                win32api.GetAsyncKeyState(win32con.VK_SHIFT) < 0 and
                win32api.GetAsyncKeyState(ord('S')) < 0):
            stop_program()
        time.sleep(0.1)