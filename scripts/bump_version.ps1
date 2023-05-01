param([String] $TagName)
Write-Host "Creating Tag named $TagName"
git tag -a $TagName -m
./generate_version.ps1