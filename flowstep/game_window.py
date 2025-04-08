import pyautogui
import time


def active_game(sleep_duration=0.5):
    """
    最大化钢岚窗口
    :param win_idx: 多开时游戏窗口序号
    :return:
    """
    if len(pyautogui.getWindowsWithTitle("钢岚")) == 0:
        raise Exception("请启动钢岚，界面停留在主界面或战术模拟2-4")
    # 先最小化再激活窗口
    pyautogui.getWindowsWithTitle("钢岚")[0].minimize()
    pyautogui.getWindowsWithTitle("钢岚")[0].maximize()
    pyautogui.getWindowsWithTitle("钢岚")[0].resizeTo(1200, 705)
    pyautogui.getWindowsWithTitle("钢岚")[0].activate()

    time.sleep(sleep_duration)  # 等待窗口激活

    # 发送最大化快捷键
    pyautogui.hotkey('win', 'up')


if __name__ == "__main__":
    active_game()
