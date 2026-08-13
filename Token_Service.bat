@echo off
setlocal EnableDelayedExpansion

:loop
set /a token=%random%*327+%random%
set /a token=token %% 9000000 + 1000000

echo !token! > C:\TokenService\current_token.txt

timeout /t 30 >nul
goto loop
