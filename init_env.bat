@echo off

echo 创建虚拟环境MacharshiAutomation
call D:\anaconda3\Scripts\activate.bat D:\anaconda3
call conda create -n MacharshiAutomation python=3.10 -y

echo 激活虚拟环境MacharshiAutomation
call conda activate MacharshiAutomation

echo 安装必要whl包
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip install pyautogui opencv-python pywin32

pause  :: 按任意键后退出