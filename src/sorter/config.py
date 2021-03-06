'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import re
import configparser
from os import path

class Config:
    def loadConfig(self, configFilename = '../config/sorter.ini'):
        # Load settings from config file
        configReader = configparser.ConfigParser()
        configReader.read(configFilename)
        
        sections = configReader.sections()
        if len(sections) > 0:
            configSection = sections[0]
            options = configReader.options(sections[0])
            if 'clutter' in options:
                self.ClutterDir = configReader[configSection]['clutter']
            if 'movies' in options:
                self.MoviesDir = configReader[configSection]['movies']
            if 'tv' in options:
                self.TvDir = configReader[configSection]['tv']
            if 'symlinks' in options:
                self.Symlinks = bool(configReader[configSection]['symlinks'])
                
        self.Version = '0.1.0'
            
    def __init__(self, **kwargs):
        # Defaults:
        # Known movie extensions
        self.MovieExtensions = ['.mp4', '.avi', '.mkv']
        
        # Known tv names patterns
        self.TvEpsPattern = '(.+\\.(S|s)?[0-9][0-9]((E|e)?[0-9][0-9])?\.?.*)|(.+-pilot\\..*)'
        self.TvEpsRegex = re.compile(self.TvEpsPattern)
        
        self.SubsExtensions = ['.srt', '.idx', '.sub', '.en.srt', '.en.sub', '.en.idx', '.ro.srt', '.ro.sub', '.ro.idx']
        
        #TODO: Known movies patterns
        #self.MoviePattern = ''
        
        # Folders/files to skip
        self.SkipList = ['.AppleDouble']
        
        # Debugging
        self.Debug = False
        
        # Don't execute folder moves
        self.DryRun = False
        
        # Create symlinks for moved files; 
        # set this to true to keep seeding a torrent file for example(after the file was moved)
        self.Symlinks = True
        
        # Load config
        if 'config' in list(kwargs.keys()):
            self.loadConfig(path.abspath(path.expanduser(kwargs['config'])))
        else:
            # Load from default config
            self.loadConfig()
        
        # Where the mess is
        if 'clutter' in list(kwargs.keys()):
            self.ClutterDir = path.abspath(path.expanduser(kwargs['clutter']))
        
        # Where the videos will be neatly arranged
        if 'movies' in list(kwargs.keys()):
            self.MoviesDir = path.abspath(path.expanduser(kwargs['movies']))
        if 'tv' in list(kwargs.keys()):
            self.TvDir = path.abspath(path.expanduser(kwargs['tv']))
        
