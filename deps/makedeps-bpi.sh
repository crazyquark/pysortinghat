#!/bin/bash
UNAME = `shell uname` 

echo "Installing Python deps, requires sudo pass please type it..." 
apt-get install python3-pip
pip-3.2 install termcolor 
pip-3.2 install rarfile
pip-3.2 install guessit

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
cp ../libunrar.dylib /usr/lib/
else
cp libunrar.so /usr/lib/
fi
