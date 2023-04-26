@echo off
echo Starting build script
nuitka --standalone --onefile --include-package=game_lib --include-data-dir=assets -o "rogers_revenge.exe" main.py