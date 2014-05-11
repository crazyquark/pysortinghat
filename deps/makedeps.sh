#!/bin/bash
UNAME = `shell uname` 

echo "Installing Python deps, requires sudo pass please type it..." 
sudo easy_install3 termcolor 
sudo easy_install3 rarfile

echo "Get UnRAR src..."
wget ftp://ftp.rarlabs.com/rar/unrarsrc-5.0.12.tar.gz

echo "Compiling libunrar..."
tar xzvf unrarsrc-*.tar.gz
cd unrar

make lib
if [[ $UNAME == *Darwin* ]]; then
mv libunrar.so ../libunrar.dylib
fi

echo "Move it in the right place..."
if [[ $UNAME == *Darwin* ]]; then
sudo cp ../libunrar.dylib /usr/lib/
else
sudo cp libunrar.so /usr/lib/
fi
