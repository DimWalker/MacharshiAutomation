import logging
import os
import time

import numpy as np
import cv2
import pyautogui

from common.func_ctypes import left_mouse_click

current_file = os.path.abspath(__file__)
target_imgs_root_path = os.path.join(os.path.dirname(os.path.dirname(current_file)), "assets", "target_imgs")


def read_image_chinese(file_path):
    """读取中文路径的图片"""
    with open(file_path, "rb") as f:
        content = f.read()
    img_array = np.asarray(bytearray(content), dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img


def find_icon_center(img_name, img_dir=None, confidence=0.8):
    if img_dir is None:
        img_path = os.path.join(target_imgs_root_path, img_name)
    else:
        img_path = os.path.join(img_dir, img_name)

    img = read_image_chinese(img_path)
    try:
        location = pyautogui.locateCenterOnScreen(img, confidence=confidence, grayscale=True)
        logging.info(f"{img_name} 图标中心坐标：{location}")
    except Exception as e:
        location = None
        logging.info(f"{img_name}，未找到图标 ")
        # 捕获其他所有类型的异常
        # logging.info(f"发生未知错误：{e}")
    finally:
        return location


def desktop_test():
    pyautogui.hotkey('win', 'd')
    time.sleep(1)
    img_name = "桌面测试图片.png"
    find_icon_center(img_name)


if __name__ == "__main__":
    desktop_test()
    pyautogui.dragTo
