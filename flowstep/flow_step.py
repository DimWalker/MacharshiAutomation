import logging
import time

# from common.func_ctypes import drag_from_center_to_left
from common.func_pyautogui import find_icon_center
from common.func_win32 import left_mouse_click, drag_from_center_to_left


def click_icon(img_name, confidence=0.8, click=True):
    location = find_icon_center(img_name, confidence=confidence)
    if location is not None:
        if click:
            left_mouse_click(location.x, location.y)
        return True
    else:
        return False


def find_icon(img_name, confidence=0.8):
    # 这个写法差差点意思
    return click_icon(img_name, confidence, False)


def auto_retry(img_name, confidence=0.8, click=True
               , retry_times=6, sleep_duration=0.5):
    for i in range(retry_times):
        flag = click_icon(img_name, confidence, click)
        if flag:
            break
        else:
            time.sleep(sleep_duration)
    return flag


def battle_center_to_battle_simulation():
    # 主界面、作战中心、拓展委托、战术模拟
    auto_retry("作战中心.png")
    auto_retry("拓展委托.png")
    flag = auto_retry("精英战役.png", click=False)
    if flag:
        # 可能需要往左拖拽
        # 太快可能界面未刷新而无法拖拽，需要等待
        time.sleep(2)
        drag_from_center_to_left(600, 370, -200)
    auto_retry("战术模拟.png")

    # 找打第一页

    for i in range(100):
        flag = auto_retry("左三角.png")
        time.sleep(0.1)
        if not flag:
            break

    auto_retry("右三角.png")

    auto_retry("常规-2-4-dis.png", confidence=0.9)


def battle_execute(number_of_battles):
    # 作战次数循环
    for n in range(number_of_battles):
        logging.info(f"战斗进度：{n}/{number_of_battles}")

        auto_retry("重新模拟.png")
        auto_retry("开始战斗.png", retry_times=30, sleep_duration=0.1)
        auto_retry("自动.png", retry_times=30)
        auto_retry("作战成功.png", retry_times=30)


def battle_simulation(number_of_battles):
    if not auto_retry("常规-2-4-dis.png", confidence=0.9, retry_times=3):
        battle_center_to_battle_simulation()
    battle_execute(number_of_battles)
