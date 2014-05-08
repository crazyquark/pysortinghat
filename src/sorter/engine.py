'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import os

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
        print 'Analyzing ', dirpath
        
        # Get dir name only
        dname = os.path.basename(dirpath)
        
        # Match against tv episodes regex
        match = self.SortConfig.TvEpsRegex.match(dname)
        if match:
            print 'Found TV content: ', dname
        else:
            # Could it be a movie?
            filesInFolder = os.listdir(dirpath)
            foundMovie = False
            for fname in filesInFolder:
                if foundMovie:
                    break
                for ext in self.SortConfig.MovieExtensions:
                    if fname.endswith(ext):
                        print 'Found Movie folder: ', dname
                        foundMovie = True
                        break
                    
    def analyzeFile(self, fname):
        pass
