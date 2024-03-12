
@echo off
echo Clone git-utils
git clone "https://github.com/bmLucasMorante/git-utils" "%USERPROFILE%\Desktop\_Repos\git-utils"

echo Adding bashrc.cmd hook to CMD
reg add "HKCU\SOFTWARE\Microsoft\Command Processor" /v AutoRun /t REG_EXPAND_SZ /d "%USERPROFILE%\Desktop\_Repos\git-utils\scripts\bashrc.cmd" /f

