@echo off

title Cyberdrop-DL
goto set_vars

:set_vars
set loop_count=0
set loop_limit=10

title Cyberdrop-DL -- %~n0 
pushd %~dp0
goto update

:update
python py/upgrade_pip_package.py cyberdrop-dl & cls
python py/latest_thread_to_urls.py & cls
python py/archive_logs.py & cls

set cdl_ver=
for /f "tokens=2 delims= " %%a in ('cyberdrop-dl --version') do set "cdl_ver=%%~a"
goto download

:download
title %cdl_ver%: Looped (%loop_count%) times. -- %time%
cyberdrop-dl --config-file config.yaml
goto loop

:loop
set /a loop_count=%loop_count%+1 
if "%loop_count%" == "%loop_limit%" goto end
goto update

:end
echo Sleeping for 3 hours...
timeout /t 10800 /nobreak
set loop_count=0
goto update
