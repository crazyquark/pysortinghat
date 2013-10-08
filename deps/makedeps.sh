#!/bin/bash

echo "Installing Python deps, requires sudo pass please type it..."
sudo easy_install termcolor
sudo easy_install rarfile

echo "Get UnRAR src..."
wget ftp://ftp.rarlabs.com/rar/unrarsrc-5.0.12.tar.gz

echo "Compiling libunrar..."
tar xzvf unrarsrc-*.tar.gz
cd unrar

make lib
mv libunrar.so ../libunrar.dylib

echo "Move it in the right place..."
sudo cp ../libunrar.dylib /usr/lib/
