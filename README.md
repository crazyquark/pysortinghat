pysortinghat
============

The Sorting Hat: a small python script for organizing your movies library. No GUI right now.
Originally on github.com.  

For the record, only movie processing works now, the rest is WIP(TV shows for example).  
Uses Python3, because, you know, it's the Future(and terminators roam the planet).

Requirements
------------
Python 3.2+ and:  
- termcolor package  
- rarfile package which also needs libunrar for all platforms  
- guessit package  
- uses ss package converted to python3 as submodule, please don't install it 
- see https://pypi.python.org/pypi/rarfile/2.2  
- You will probably need to build from source, see ftp://ftp.rarlabs.com/rar/  
-----
- Check out the script deps/makedeps.sh for an automated way to install dependencies(OS X and Linux only)  