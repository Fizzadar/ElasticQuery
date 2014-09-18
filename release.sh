#!/usr/bin/env bash

VERSION=`./setup.py --version`
echo "Version: $VERSION"

echo "Doing git..."
git tag -a "v$VERSION" -m "v$VERSION"
git push
git push --tags

echo "Publishing to pypi"
./setup.py sdist upload
