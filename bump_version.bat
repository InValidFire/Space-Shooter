@echo off
@REM echo Creating Tag named %1
@REM git tag -a %1 -m "%1"
@REM echo Sending tag to origin
@REM git push origin %1
echo Creating version file
@REM set /p will remove preceding spaces
echo | set /p pre_text="‎hash: " > ./assets/version
git log --format="%%h" -n 1 >> ./assets/version
echo | set /p commit_pre_text="build: " >> ./assets/version
echo %1>> ./assets/version