import time

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


if __name__ == '__main__':
    active_game()
    # 等待窗口激活
    time.sleep(1)
    # 战斗循环20次，手动修改
    battle_simulation(20)
