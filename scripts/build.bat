@echo off
call bump_version %1
echo Starting build script
rmdir build /s /q
pyxel package . main.py
pyxel app2html rogers_revenge.pyxapp
move rogers_revenge.pyxapp dist
move rogers_revenge.html dist
nuitka --standalone --onefile --include-package=game_lib --windows-disable-console --include-data-dir=assets=assets --output-dir=build --output-filename="dist/rogers_revenge.exe" main.py