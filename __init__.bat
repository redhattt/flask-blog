@echo off

:choice
set /p q=Do you want to run on PRODUCTION mode[Y/N]?

if /i "%q%" equ "y" goto :opt_yes
if /i "%q%" equ "n" goto :opt_no

goto :choice

:opt_yes
waitress-serve --host 0.0.0.0 --port 8080 app:server

:opt_no
flask run --debug --port 8080