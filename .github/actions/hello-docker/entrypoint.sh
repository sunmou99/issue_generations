#!/bin/sh

set -ex

python test.py
echo "::error :: Error message"
echo "Hello World"

echo "Hola $1"


