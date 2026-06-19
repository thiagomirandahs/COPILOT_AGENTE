@echo off
title Adir Chat
cd /d "%~dp0"
echo Iniciando o servidor do Adir Chat...
start "Adir Chat - servidor" cmd /k node server.js
timeout /t 2 >nul
start "" http://localhost:3000
echo.
echo Abrindo no navegador: http://localhost:3000
echo (Para parar, feche a janela "Adir Chat - servidor".)
