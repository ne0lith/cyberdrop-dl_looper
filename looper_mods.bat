@echo off
setlocal enabledelayedexpansion

pushd "%~dp0"

REM User Config
set "loop_count=20"
set "profile_name=Default"
set "backup_logs=true"
set "send_webhook=false"

for /L %%i in (1, 1, %loop_count%) do (
    echo Running iteration %%i
    call :RunSubBatch

    REM Call Postrun functions

    REM Backup all logs each run (this can take up GIGS in no time. be sure to delete every once in a while.)
    if "%backup_logs%"=="true" (
        python mods\file_management.py "!profile_name!"
    )

    REM Send a discord webhook to notify you of final numbers
    if "%send_webhook%"=="true" (
        call :RunPythonScript "mods\send_webhook_results.py" "!profile_name!"
    )
)

popd
goto :eof

:RunSubBatch
start /wait "Cyberdrop-DL" "Start Windows.bat"
timeout /t 3 /nobreak >nul
goto :eof

pause
