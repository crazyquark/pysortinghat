'''
Created on Sep 30, 2012

@author: Cristian Sandu
'''

import os
import shutil
import glob
import re

import rarfile

from termcolor import cprint

class Cleaner:
    ''' Cleaner un-archives movies, moves subs around, makes it all nice '''
    ''' Uses unrar lib from https://pypi.python.org/pypi/rarfile/2.6 '''
    def __init__(self, config):
        self.SortConfig = config
    
    def cleanTvDir(self):
        pass
    
    def cleanMoviesDir(self):
        ''' Time to clean! '''
        if (not os.path.isdir(self.SortConfig.MoviesDir)):
            return
        
        filelist = os.listdir(self.SortConfig.MoviesDir)
        
        for fname in filelist:
            filepath = os.path.join(self.SortConfig.MoviesDir, fname)
            if os.path.isfile(filepath):
                self.processMovieFile(fname)
            elif os.path.isdir(filepath):
                self.processMovieDir(fname)
     
    def processMovieFile(self, fname):
        ''' Make a directory for orphan .AVIs '''
        isMovie = False
        for ext in self.SortConfig.MovieExtensions:
            if (fname.endswith(ext)):
                isMovie = True
                break
        
        if (not isMovie):
            # Probably not a movie file, leave it alone
            return
        
        # Get only the filename
        dname = os.path.splitext(fname)[0]
        
        # Make directory
        target = self.SortConfig.MoviesDir + os.sep + dname
        if not os.path.exists(target):
            os.mkdir(self.SortConfig.MoviesDir + os.sep + dname)
        
        # Move file to directory
        source = self.SortConfig.MoviesDir + os.sep + fname
        shutil.move(source, target)
        print 'Moved ',fname, 'to ', target
        
    def processMovieDir(self, dname):
        ''' Un-archive files, make nice '''
        crtDir = self.SortConfig.MoviesDir + os.sep + dname
        cprint('Processing ' + crtDir, 'green')
        
        # Search for rar files
        targetPattern = re.escape(crtDir) + os.sep + '*.rar'
        if self.SortConfig.Debug:
            print 'Pattern: ', targetPattern
        
        cleanPattern = re.escape(crtDir) + os.sep + '*.r[0-9][0-9]'
        for rarfilename in glob.glob(targetPattern):
            if rarfile.is_rarfile(rarfilename):
                print 'Found rarfile', rarfilename
                print 'Extracting ...',
                # extract
                rarfile = rarfile.RarFile(rarfilename)
                rarfile.extractall(crtDir)
                print 'done!'
                print 'Deleting ', rarfilename
                os.remove(rarfilename)
                
        # Delete all .rXX files
        for rarfilename in glob.glob(cleanPattern):
                # delete
                print 'Deleting ', rarfilename
                os.remove(rarfilename)
        
        # Process subs if they exists        
        subsDir = crtDir + os.sep + 'Subs'
        if (os.path.exists(subsDir)):
            # Need to process subs as well
            print 'Processing subtitles dir'
            subsRarPattern = re.escape(subsDir) + os.sep + '*.rar'
            for subsRarfilename in glob.glob(subsRarPattern):
                # Extract subtitles
                if rarfile.is_rarfile(subsRarfilename):
                    print 'Extracting ', subsRarfilename, '...',
                    subsRarfile = rarfile.RarFile(subsRarfilename)
                    subsRarfile.extractall(crtDir)
                    print 'done!'
                    #Remove it
                    print 'Deleting ', subsRarfilename
                    os.remove(subsRarfilename)
                    
                    # Extract idx if it exists
                    for idxRarfilename in glob.glob(subsRarfilename):
                        if rarfile.is_rarfile(idxRarfilename):
                            print 'Extracting ', idxRarfilename, '...',
                            idxRarfile = rarfile.RarFile(idxRarfilename)
                            idxRarfile.extractall(crtDir)
                            print 'done!'
                            # Remove it
                            os.remove(idxRarfilename)
            
            # Delete subs dir
            print 'Deleting ', subsDir
            shutil.rmtree(subsDir)
