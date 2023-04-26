@echo off
@REM echo Creating Tag named %1
@REM git tag -a %1 -m "%1"
@REM echo Sending tag to origin
@REM git push origin %1
echo Creating version file
git log --format="%%h" -n 1 > ./assets/version
echo %1>> ./assets/version