param([String] $TagName)
Write-Host "Creating Tag named $TagName"
git tag -a $TagName -m $TagName