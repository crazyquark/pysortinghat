'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import os
from termcolor import cprint

class SortingEngine:
    def __init__(self, config):
        self.SortConfig = config

    def sort(self):
        '''
        Analyze cluttered dir, find movies
        '''
        filelist = os.listdir(self.SortConfig.ClutterDir)
        for fname in filelist:
            filepath = os.path.join(self.SortConfig.ClutterDir, fname)
            
            if (os.path.isfile(filepath)):
                self.analyzeFile(filepath)
            elif (os.path.isdir(filepath)):
                self.analyzeDir(filepath)

    def analyzeDir(self, dirpath):
        '''
        Analyze directory name
        '''
        cprint ('Analyzing ' + str(dirpath), 'green')
        
        # Get dir name only
        dname = os.path.basename(dirpath)
        
        # Match against tv episodes regex
        match = self.SortConfig.TvEpsRegex.match(dname)
        if match:
            cprint('Found TV content: ' + dname, 'red')
        else:
            # Could it be a movie?
            filesInFolder = os.listdir(dirpath)
            foundMovie = False
            for fname in filesInFolder:
                if foundMovie:
                    break
                for ext in self.SortConfig.MovieExtensions:
                    if fname.endswith(ext):
                        cprint ('Found Movie folder: ' + dname, 'red')
                        foundMovie = True
                        break
                    
    def analyzeFile(self, fname):
        pass
