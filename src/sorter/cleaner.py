'''
Created on Sep 30, 2012

@author: Cristian Sandu
'''

import os
import shutil
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
        
        dname = os.path.basename(fname)
        
        # Make directory
        os.mkdir(self.TargetDir + os.sep + dname)
        
        # Move file to directory
        shutil.move(fname, self.TargetDir + os.sep + dname)
        
    def processDir(self, dname):
        ''' Un-archive files, make nice '''
        pass
