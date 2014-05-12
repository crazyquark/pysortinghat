'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import re
import ConfigParser

class Config:
    def loadConfig(self, configFilename = '../config/sorter.ini'):
        # Load settings from config file
        configReader = ConfigParser.ConfigParser()
        configReader.read(configFilename)
        
        sections = configReader.sections()
        if len(sections) > 0:
            options = configReader.options(sections[0])
            if 'Clutter' in options.keys():
                self.ClutterDir = options['Clutter']
            if 'Movies' in options.keys():
                self.MoviesDir = options['Movies']
            if 'TV' in options.keys():
                self.TvDir = options['TV']
            
    def __init__(self, **kwargs):
        if 'config' in kwargs.keys():
            self.loadConfig(kwargs['config'])
        else:
            # Load from default config
            self.loadConfig()
        # Where the mess is
        if 'clutter' in kwargs.keys():
            self.ClutterDir = kwargs['clutter']
        
        # Where the videos will be neatly arranged
        if 'movies' in kwargs.keys():
            self.MoviesDir = kwargs['movies']
        if 'tv' in kwargs.keys():
            self.TvDir = kwargs['tv']
        
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
