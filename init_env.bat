@echo off

echo �������⻷��MacharshiAutomation
call D:\anaconda3\Scripts\activate.bat D:\anaconda3
call conda create -n MacharshiAutomation python=3.10 -y

echo �������⻷��MacharshiAutomation
call conda activate MacharshiAutomation

echo ��װ��Ҫwhl��
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
pip install pyautogui opencv-python pywin32

pause  :: ����������˳�