# Moved  

Moved here: [https://github.com/cristianghsandu/pysortinghat](https://github.com/cristianghsandu/pysortinghat)  

pysortinghat
============

The Sorting Hat: a small python script for organizing your movies library. No GUI right now.

Uses Python3, because, you know, it's the Future(and terminators roam the planet).

I use it on my Raspberry Pi and Banana Pi to organize my shared media library.  

Requirements
------------
Python 3.2+ and:  
- termcolor package  
- guessit package  
- uses ss package converted to python3 as submodule, please don't install it  
- rarfile package which needs a working libunrar  
- see https://pypi.python.org/pypi/rarfile/2.2  
- You will probably need to build from source, see ftp://ftp.rarlabs.com/rar/  

Changelog
---------
Version 0.1.0
- implemented TV episodes sorting using guessit

-----
- Check out the script deps/makedeps.sh for an automated way to install dependencies(OS X and Linux only)
