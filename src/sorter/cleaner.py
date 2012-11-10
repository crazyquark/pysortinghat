'''
Created on Sep 30, 2012

@author: Cristian Sandu
'''

import os
import shutil
import glob

import unrar

from config import Config

class Cleaner:
    ''' Cleaner un-archives movies, moves subs around, makes it all nice '''
    ''' Use unrar lib from https://github.com/matiasb/python-unrar '''
    def __init__(self, targetDir = 'G:\\Movies'):
        self.TargetDir = targetDir
        
    def clean(self):
        ''' Time to clean! '''
        filelist = os.listdir(self.TargetDir)
        
        for fname in filelist:
            filepath = os.path.join(self.TargetDir, fname)
            if os.path.isfile(filepath):
                self.processFile(fname)
            elif os.path.isdir(filepath):
                self.processDir(fname)
     
    def processFile(self, fname):
        ''' Make a directory for orphan .AVIs '''
        isMovie = False
        for ext in Config.MovieExtensions:
            if (fname.endswith(ext)):
                isMovie = True
                break
        
        if (not isMovie):
            # Probably not a movie file, leave it alone
            return
        
        # Get only the filename
        dname = os.path.basename(fname)
        
        # Make directory
        os.mkdir(self.TargetDir + os.sep + dname)
        
        # Move file to directory
        target = self.TargetDir + os.sep + dname
        shutil.move(fname, target)
        print 'Moved ',fname, 'to ', target
        
    def processDir(self, dname):
        ''' Un-archive files, make nice '''
        for rarfilename in glob.glob(dname + os.sep + '*.rar'):
            if unrar.rarfile.is_rarfile(rarfilename):
                # extract
                rarfile = unrar.rarfile.RarFile(rarfilename)
                rarfile.extractall()
                
                # delete
                os.remove(rarfilename)
                
