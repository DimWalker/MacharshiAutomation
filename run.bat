@echo off
:: 需要管理员权限的操作
fsutil dirty query %SystemDrive% >nul 2>&1
if %errorlevel% == 0 (
    echo 当前已是管理员权限！
) else (
    echo 未以管理员权限运行，请右键"以管理员身份运行"！
    pause
    exit /b
)

echo 你有3秒时间，把当前cmd窗口拖到左下角
echo 不拖也没关系，就是可能看不到日志而已
echo 程序正式运行后，会循环20次战斗
echo 运行期间不要动鼠标键盘等
echo 中途可按ctrl + shift + s强制退出
timeout /t 3

:: 激活conda环境
call D:\anaconda3\Scripts\activate.bat D:\anaconda3
call conda activate MacharshiAutomation

:: 切换到脚本所在目录
cd /d "%~dp0"
python main.py

pause  :: 按任意键后退出