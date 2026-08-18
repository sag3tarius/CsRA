@echo off
setlocal EnableDelayedExpansion

:loop
set /a token=%random%*327+%random%
set /a token=token %% 9000000 + 1000000

echo !token! > C:\TokenService\current_token.txt

REM Send token to Linux using SCP on custom SSH port
scp -P 62579 C:\TokenService\current_token.txt root@LINUX_HOST:/bin/tkn

timeout /t 30 >nul
goto loop
