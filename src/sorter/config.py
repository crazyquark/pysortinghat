'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import re

class Config:
    def __init__(self, clutterDir, moviesDir, tvDir):
        # Where the mess is
        self.ClutterDir = clutterDir
        # Where the videos will be neatly arranged
        self.MoviesDir = moviesDir
        self.TvDir = tvDir
        
        # Known movie extensions
        self.MovieExtensions = ['.mp4', '.avi', '.mkv']
        
        # Known tv names patterns
        self.TvEpsPattern = '.+\\.S[0-9][0-9](E[0-9][0-9])?\.?.*'
        self.TvEpsRegex = re.compile(self.TvEpsPattern)
        
        #TODO: Known movies patterns
        #self.MoviePattern = ''
        
        # Folders/files to skip
        self.SkipList = ['.AppleDouble']
        
        # Debugging
        self.Debug = False
        
        # Don't execute folder moves
        self.DryRun = False
