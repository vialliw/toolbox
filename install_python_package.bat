@echo off
SET new_package_name=%1
echo new_package_name=%new_package_name%

set /p confirm=Are you sure you want to install %new_package_name%? (Y/N): 
if /i "%confirm%" neq "Y" (
    echo Operation cancelled.
    exit /b
)

py -m pip show %new_package_name%
if %ERRORLEVEL%==0 (
    py -m pip show %new_package_name% > %new_package_name%.log
    echo Package %new_package_name% is installed.  See log file: %new_package_name%.log
) else (
    py -m pip install %new_package_name%
)
pause
