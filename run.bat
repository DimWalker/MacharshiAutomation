@echo off
:: ��Ҫ����ԱȨ�޵Ĳ���
fsutil dirty query %SystemDrive% >nul 2>&1
if %errorlevel% == 0 (
    echo ��ǰ���ǹ���ԱȨ�ޣ�
) else (
    echo δ�Թ���ԱȨ�����У����Ҽ�"�Թ���Ա�������"��
    pause
    exit /b
)

echo ����3��ʱ�䣬�ѵ�ǰcmd�����ϵ����½�
echo ����Ҳû��ϵ�����ǿ��ܿ�������־����
echo ������ʽ���к󣬻�ѭ��20��ս��
echo �����ڼ䲻Ҫ�������̵�
echo ��;�ɰ�ctrl + shift + sǿ���˳�
timeout /t 3

:: ����conda����
call D:\anaconda3\Scripts\activate.bat D:\anaconda3
call conda activate MacharshiAutomation

:: �л����ű�����Ŀ¼
cd /d "%~dp0"
python main.py

pause  :: ����������˳�