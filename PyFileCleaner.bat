@echo off
chcp 65001 > nul
title PyFileCleaner

echo =====================================
echo  PyFileCleaner - Organizando arquivos
echo =====================================
echo.

REM Caminho do Python
set PYTHON_PATH=C:\Users\lucas\AppData\Local\Programs\Python\Python314\python.exe

REM Pasta do projeto (onde está o .bat)
set PROJECT_PATH=%~dp0

cd /d "%PROJECT_PATH%"

echo Executando script...
echo.

"%PYTHON_PATH%" "src\main.py"

echo.
echo =====================================
echo  Execucao finalizada
echo =====================================
echo.

pause
