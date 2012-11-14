'''
Created on Sep 30, 2012

@author: Cristian Sandu
'''

import os
import shutil
import glob

import unrar.rarfile

from config import Config

class Cleaner:
    ''' Cleaner un-archives movies, moves subs around, makes it all nice '''
    ''' Use unrar lib from https://github.com/matiasb/python-unrar '''
    def __init__(self, config):
        self.ConfigObj = config
        
    def clean(self):
        ''' Time to clean! '''
        filelist = os.listdir(self.ConfigObj.MoviesDir)
        
        for fname in filelist:
            filepath = os.path.join(self.ConfigObj.MoviesDir, fname)
            if os.path.isfile(filepath):
                self.processFile(fname)
            elif os.path.isdir(filepath):
                self.processDir(fname)
     
    def processFile(self, fname):
        ''' Make a directory for orphan .AVIs '''
        isMovie = False
        for ext in self.ConfigObj.MovieExtensions:
            if (fname.endswith(ext)):
                isMovie = True
                break
        
        if (not isMovie):
            # Probably not a movie file, leave it alone
            return
        
        # Get only the filename
        dname = os.path.splitext(fname)[0]
        
        # Make directory
        target = self.ConfigObj.MoviesDir + os.sep + dname
        if not os.path.exists(target):
            os.mkdir(self.ConfigObj.MoviesDir + os.sep + dname)
        
        # Move file to directory
        source = self.ConfigObj.MoviesDir + os.sep + fname
        shutil.move(source, target)
        print 'Moved ',fname, 'to ', target
        
    def processDir(self, dname):
        ''' Un-archive files, make nice '''
        crtDir = self.ConfigObj.MoviesDir + os.sep + dname
        targetPattern = crtDir + os.sep + '*.rar'
        cleanPattern = crtDir + os.sep + '*.r[0-9][0-9]'
        for rarfilename in glob.glob(targetPattern):
            if unrar.rarfile.is_rarfile(rarfilename):
                print 'Found rarfile', rarfilename, ": extracting!"
                # extract
                rarfile = unrar.rarfile.RarFile(rarfilename)
                rarfile.extractall(crtDir)
                print 'Done!'
                print 'Deleting ', rarfilename
                #os.remove(rarfilename)
        # Delete all .rXX files
        for rarfilename in glob.glob(cleanPattern):
                # delete
                print 'Deleting ', rarfilename
                #os.remove(rarfilename)
                
