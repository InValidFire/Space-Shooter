echo Creating Tag named $1
git tag -a $1 -m
./generate_version.sh