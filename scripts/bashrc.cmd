@echo off
REM This file runs with every terminal.

REM Hook to user-configuration:
REM In this file we add some global aliases

REM General OS
doskey ls=dir
doskey home=cd %USERPROFILE%
doskey pipe=cd c:/works/git

REM Python & venvs
doskey activate=".venv/Scripts/activate"

REM git utils
doskey dev-config-check=echo "Checking dev configuration integrity..."

REM Hook to user-configuration:
rem ../user/../bashrc_local.cmd
