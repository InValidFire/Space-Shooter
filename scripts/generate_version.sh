#!/usr/bin/bash
echo "Creating version file"
echo " hash: $(git log --format="%h" -n 1)" > ./assets/version
echo "build: $(git describe --abbrev=0)" >> ./assets/version