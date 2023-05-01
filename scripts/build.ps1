echo "Starting build script"
if (Test-Path ".\build") {
    Remove-Item -Path ".\build" -Recurse
    Write-Host "Folder .\build removed."
}
.\scripts\generate_version.ps1
Write-Host "Packaging Pyxel application"
pyxel package . main.py
Write-Host "Exporting Pyxel application to HTML"
pyxel app2html rogers_revenge.pyxapp
if (Test-Path ".\dist") {
    New-Item -Path ".\dist" -ItemType Directory
    Write-Host "Folder .\dist created."
}
Move-Item -Path "rogers_revenge.pyxapp" -Destination ".\dist\rogers_revenge.pyxapp"
Move-Item -Path "rogers_revenge.html" -Destination ".\dist\rogers_revenge.html"
nuitka3 --standalone --onefile --include-data-dir=assets=assets --include-package=game_lib --output-dir=build --output-filename=rogers_revenge.exe main.py
Move-Item -Path ".\build\rogers_revenge.exe .\dist\rogers_revenge.exe"
