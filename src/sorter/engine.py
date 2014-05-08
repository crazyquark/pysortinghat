'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import os
import shutil
from termcolor import cprint

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
                SortingEngine.movieFile(self.SortConfig, dname, True)
                    
    def processFile(self, fname):
        # Not yet
        pass
    
    @staticmethod
    def movieFile(config, dname, isMovie):
        '''
        Moves a file/folder recursively from their current location to proper target dir(Movies/TV)
        '''
        if config.DryRun:
            return
        
        # Make directory
        target = config.MoviesDir + os.sep + dname
        if not os.path.exists(target):
            os.mkdir(config.MoviesDir + os.sep + dname)
        
        # Move file to directory
        source = config.MoviesDir + os.sep + dname if isMovie else config.TvDir + os.sep + dname
        if (os.path.isfile(source)):
            shutil.move(source, target)
        else:
            # This is needed in case some previous failed attempt created this folder
            if (os.path.exists(target)):
                cprint("Warning: target dir exists, deleting!", 'yellow')
                shutil.rmtree(target)
            shutil.copytree(source, target)
            shutil.rmtree(source)
        print 'Moved ',dname, 'to ', target
