@echo off
setlocal enabledelayedexpansion

pushd "%~dp0"

REM User Config
set "loop_count=20"

for /L %%i in (1, 1, %loop_count%) do (
    echo Running iteration %%i
    call :RunSubBatch
)

goto :eof

:RunSubBatch
start /wait "Cyberdrop-DL" "start.bat"
timeout /t 3 /nobreak >nul
goto :eof

pause
