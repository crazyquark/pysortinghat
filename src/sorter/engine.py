'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import os

class SortingEngine:
    def __init__(self, config):
        self.ConfigObj = config

    def analyze(self):
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
        pass