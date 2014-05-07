'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import os

class SortingEngine:
    def __init__(self, config):
        self.ConfigObj = config

    def sort(self):
        '''
        Analyze cluttered dir, find movies
        '''
        filelist = os.listdir(self.ConfigObj.ClutterDir)
        for fname in filelist:
            filepath = os.path.join(self.ConfigObj.ClutterDir, fname)
            
            if (os.path.isfile(filepath)):
                self.analyzeFile(filepath)
            elif (os.path.isfile(filepath)):
                self.analyzeDir(filepath)

    def analyzeDir(self, dirpath):
        '''
        Analyze directory name
        '''
        print 'Analyzing ', dirpath
        
        # Get dir name only
        dname = os.path.splitext(dirpath)[0]
        
        # Match against tv episodes regex
        match = self.ConfigObj.TvEpsRegex.match(dname)
        if match:
            print 'Found TV content: ', dname
            
    def analyzeFile(self, fname):
        pass
