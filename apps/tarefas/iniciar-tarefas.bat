@echo off
title App de Tarefas - Adir
cd /d "%~dp0"
echo Instalando dependencias (so na primeira vez)...
python -m pip install -r requirements.txt
echo.
echo Iniciando o servidor em http://localhost:8077
start "" http://localhost:8077
python -m uvicorn main:app --port 8077
pause
