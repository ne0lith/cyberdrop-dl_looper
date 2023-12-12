@echo off
setlocal enabledelayedexpansion

pushd "%~dp0"

REM Read config from file
for /f "delims=" %%a in (config.txt) do set %%a

for /L %%i in (1, 1, %loop_count%) do (
    echo Running iteration %%i of %loop_count%
    call :RunSubBatch

    if "%backup_logs%"=="true" (
        python "mods\file_management.py" "!profile_name!"
    )
    if "%send_webhook%"=="true" (
        python "mods\send_webhook_results.py" "!profile_name!" "!machine_name!"
    )

    echo Completed iteration %%i of %loop_count%
    echo .
    echo Sleeping for !sleep_time! seconds before the next iteration...
    timeout /t !sleep_time! /nobreak
)

goto :eof

:RunSubBatch
start /wait "Cyberdrop-DL" "start.bat"
timeout /t 3 /nobreak >nul
goto :eof

pause
