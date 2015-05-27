#!/bin/sh

VERSION=`python setup.py --version`

echo "# Releasing ElasticQuery v$VERSION..."

echo "# Doing git..."
git tag -a v$VERSION -m v$VERSION
git push --tags

echo "# Doing pypi..."
python setup.py sdist upload

echo "# Released!"
