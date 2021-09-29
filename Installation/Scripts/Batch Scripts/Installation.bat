timeout /t 1 /nobreak > NUL

Echo Installing Python...

@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

choco install -y python3

Echo Python Installed!

timeout /t 1 /nobreak > NUL

Echo Installing Dependencies...

timeout /t 1 /nobreak > NUL

pip install -r requirements.txt

timeout /t 1 /nobreak > NUL

pip install yahoo-fin

@echo off
set /p allDone="All Done! Press 'Enter' to exit:"