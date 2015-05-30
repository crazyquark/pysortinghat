#!/bin/bash
UNAME=`uname` 

echo "Installing Python deps, requires sudo pass please type it..." 
sudo apt-get install python3 python3-setuptools
sudo easy_install3 termcolor 
sudo easy_install3 rarfile
sudo easy_install3 enzyme
sudo easy_install3 guessit

echo "Get UnRAR src..."
wget ftp://ftp.rarlabs.com/rar/unrarsrc-5.2.7.tar.gz

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

echo "Cleaning up..."
cd ../
rm -rf unrar*


