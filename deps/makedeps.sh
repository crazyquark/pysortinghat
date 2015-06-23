#!/bin/bash
UNAME=`uname` 

echo "Installing Python deps, requires sudo pass please type it..." 
apt-get install python3 python3-setuptools
easy_install3 termcolor 
easy_install3 rarfile
easy_install3 enzyme
easy_install3 guessit

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
cp ../libunrar.dylib /usr/lib/
else
cp libunrar.so /usr/lib/
fi

echo "Cleaning up..."
cd ../
rm -rf unrar*


