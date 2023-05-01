Write-Host "Creating version file"
$hash = git log --format="%h" -n 1
$build = git describe --abbrev=0
Set-Content -Path ".\assets\version" -Value " hash: $hash`nbuild: $build"