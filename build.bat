@echo off
echo Starting build script
pyxel package . main.py
pyxel app2html rogers_revenge.pyxapp
move rogers_revenge.pyxapp dist
move rogers_revenge.html dist
nuitka --standalone --onefile --include-package=game_lib --include-data-dir=assets=assets --output-filename="dist/rogers_revenge.exe" main.py