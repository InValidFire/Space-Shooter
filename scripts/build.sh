#!/usr/bin/bash
echo Starting build script
if [[ -d "./build" ]]
then
    rmdir -r ./build
    echo "Folder ./build removed."
fi
./generate_version.sh
echo "Packaging Pyxel application"
pyxel package . main.py
echo "Exporting Pyxel application to HTML"
pyxel app2html rogers_revenge.pyxapp
if [[ ! -d "./dist" ]]
then
    mkdir ./dist
    echo "Folder ./dist created."
fi
mv rogers_revenge.pyxapp dist/
mv rogers_revenge.html dist/
nuitka3 --standalone --onefile --include-data-dir=assets=assets --include-package=game_lib --output-dir=build --output-filename=rogers_revenge.bin main.py
mv build/rogers_revenge.bin dist/