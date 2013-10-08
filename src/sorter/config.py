'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import re

class Config:
    def __init__(self, clutterDir = 'G:\\Torrents',
                 moviesDir = 'G:\\Movies', tvDir = 'G:\\TV'):
        # Where the mess is
        self.ClutterDir = clutterDir
        # Where the videos will be neatly arranged
        self.MoviesDir = moviesDir
        self.TvDir = tvDir
        
        # Known movie extensions
        self.MovieExtensions = ['.mp4', '.avi', '.mkv']
        
        # Known tv names patterns
        self.TvEpsPattern = '.+\\.S[0-9][0-9](E[0-9][0-9])?\.?.*'
        self.TvExpRegex = re.compile(self.TvEpsPattern)
        
        # Known movies patterns
        self.MoviePattern = ''
        
        # Debugging
        self.Debug = True
