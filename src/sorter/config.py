'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''


class Config:
    def __init__(self, clutterDir = 'G:\\Torrents',
                 moviesDir = 'G:\\Movies', tvDir = 'G:\\TV'):
        # Where the mess is
        self.ClutterDir = clutterDir
        # Where the videos will be neatly arranged
        self.MoviesDir = moviesDir
        self.TvDir = tvDir
        
