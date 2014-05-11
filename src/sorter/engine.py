'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import os
import shutil
from termcolor import cprint

class Movie:
    '''
    A class to represent a Movie file
    '''
    def __init__(self, fname):
        self.Fname = fname

class TvShow:
    '''
    A class to represent a TV Show
    '''
    def __init__(self, name):
        self.Name = name
        self.Episodes = []

class SortingEngine:
    def __init__(self, config):
        self.SortConfig = config
    
    def sortAndMoveToTarget(self):
        '''
        Analyze cluttered dir, find movies
        '''
        filelist = os.listdir(self.SortConfig.ClutterDir)
        for fname in filelist:
            filepath = os.path.join(self.SortConfig.ClutterDir, fname)
            
            if (os.path.isfile(filepath)):
                self.processFile(filepath)
            elif (os.path.isdir(filepath)):
                self.processDir(filepath)

    def processDir(self, dirpath):
        '''
        Analyze directory name
        '''
        if self.SortConfig.Debug:
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
                
                if fname in self.SortConfig.SkipList:
                    continue
                
                for ext in self.SortConfig.MovieExtensions:
                    if fname.endswith(ext):
                        cprint ('Found Movie folder: ' + dname, 'red')
                        foundMovie = True
                        break
                    
            # Put movies in Movies folder
            if foundMovie:
                self.moveFolder(self.SortConfig, dname, True)
                    
    def processFile(self, fname):
        # Not yet
        match = self.SortConfig.TvEpsRegex.match(fname)
        if match:
            cprint ('Found TV episode: ', fname)
        else:
            for ext in self.SortConfig.MovieExtensions:
                if fname.endswith(ext):
                    # Looks like an orphaned movie? Movie it to Movies dir and let the cleaner deal with it
                    cprint ('Found orphaned movie file: ' + fname, 'green')
                    source = os.path.join(self.SortConfig.ClutterDir, fname)
                    shutil.move(source, self.SortConfig.MoviesDir)
                    cprint ('Moved ' + fname + ' to ' + self.SortConfig.MoviesDir)
                    break
                
    def moveFolder(self, dname, isMovie):
        '''
        Moves a file/folder recursively from their current location to proper target dir(Movies/TV)
        '''
        if self.SortConfig.DryRun:
            return
        
        # Make directory
        target = os.path.join(self.SortConfig.MoviesDir if isMovie else self.SortConfig.TvDir, dname)
        
        # Move file to directory
        source = os.path.join(self.SortConfig.ClutterDir, dname)
        # This is needed in case some previous failed attempt created this folder
        if (os.path.exists(target)):
            cprint("Warning: target dir exists, deleting!", 'yellow')
            shutil.rmtree(target)
        shutil.move(source, target)
        print('Moved ',dname, 'to ', target)
