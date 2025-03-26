import logging

import win32api
import win32con
import time


def left_mouse_click(x=None, y=None):
    """
    模拟鼠标左键单击操作
    :param x: 目标位置的X坐标（可选）
    :param y: 目标位置的Y坐标（可选）
    """
    if x is not None and y is not None:
        win32api.SetCursorPos((x, y))  # 移动鼠标到指定位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 模拟鼠标左键按下
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 模拟鼠标左键释放


def mouse_double_click(x=None, y=None):
    """
    模拟鼠标双击操作
    :param x: 目标位置的X坐标（可选）
    :param y: 目标位置的Y坐标（可选）
    """
    if x is not None and y is not None:
        win32api.SetCursorPos((x, y))  # 移动鼠标到指定位置
    # 模拟鼠标左键双击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 按下左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 释放左键
    time.sleep(0.05)  # 短暂延迟，模拟真实双击间隔
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 再次按下左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)  # 再次释放左键


def drag_from_center_to_left(start_x,start_y,offset_x=-100,):
    # 获取屏幕中心点坐标
    # screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    # screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    # center_x = screen_width // 2
    # center_y = screen_height // 2
    target_x = start_x + offset_x
    target_y = start_y
    logging.info(f"start_x: {start_x}, "
          f"start_y: {start_y}, "
          f"target_x: {target_x}, "
          f"target_y: {target_y}")

    win32api.SetCursorPos((start_x, start_y))
    # 1. 按下鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, start_x, start_y, 0, 0)
    time.sleep(0.01)
    # 2. 模拟拖动（分步移动更平滑）
    steps = 20  # 分 20 步移动
    for i in range(1, steps + 1):
        x = int(start_x + (i * offset_x / steps))  # 计算当前步的 x 坐标
        y = start_y
        win32api.SetCursorPos((x, y))  # 更新鼠标位置
        time.sleep(0.01)  # 短暂延迟，模拟真实拖动

    # 3. 释放鼠标左键

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, target_x, target_y, 0, 0)
