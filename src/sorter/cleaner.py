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
from guessit import guess_file_info as guessFileInfo
from sorter.engine import SortingEngine

class Cleaner:
    ''' Cleaner un-archives movies, moves subs around, makes it all nice '''
    ''' Uses unrar lib from https://pypi.python.org/pypi/rarfile/2.6 '''
    def __init__(self, config):
        self.SortConfig = config
    
    def cleanTvDir(self):
        if (not os.path.isdir(self.SortConfig.TvDir)):
            return
        
        filelist = os.listdir(self.SortConfig.TvDir)
        
        for fname in filelist:
            filepath = os.path.join(self.SortConfig.TvDir, fname)
            if os.path.isfile(filepath):
                self.processTvFile(fname)
            elif os.path.isdir(filepath):
                self.processTvDir(fname)
    
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
    
    def processTvFile(self, fname):
        ''' Moves orphan TV episode files to the proper folder and fixes symlinks'''
        ext = os.path.splitext(fname)[1]
        if ext in self.SortConfig.SubsExtensions:
            return # will deal with you later, mister!
        
        availableShowDirs = os.listdir(self.SortConfig.TvDir)
        
        guessedInfoDict = guessFileInfo(fname, info=['filename'])
        if 'series' in guessedInfoDict:
            possibleShowName = guessedInfoDict['series'].title() # Make first letter caps, like in "Supernatural"
        
            if possibleShowName in availableShowDirs:
                self.moveEpisodeFile(fname, possibleShowName)
                return
            elif 'year' in guessedInfoDict:
                possibleShowName = possibleShowName + ' ' + str(guessedInfoDict['year'])
                if possibleShowName in availableShowDirs:
                    self.moveEpisodeFile(fname, possibleShowName)
                    return
            
            # A new show folder? Oh, joy!
            if possibleShowName:
                target = os.path.join(self.SortConfig.TvDir, possibleShowName)
                os.mkdir(target)
                self.moveEpisodeDir(fname, possibleShowName)
                
    def processSubs(self, fname, source, targetDir):
        for subExt in self.SortConfig.SubsExtensions:
            subFname = os.path.splitext(fname)[0] + subExt
            # Move subtitle to the Movies folder
            
            source = os.path.join(self.SortConfig.TvDir, subFname)
            if os.path.exists(source):
                shutil.move(source, targetDir)
                cprint('Moved ' + subFname + ' to ' + targetDir, 'yellow')
    
    def moveEpisodeFile(self, fname, showName):
        source = os.path.join(self.SortConfig.TvDir, fname)
        target = os.path.join(self.SortConfig.TvDir, showName)
        
        shutil.move(source, target)
        cprint('Moved ' + fname + ' to ' + target, 'red')
        
        # Fix possible dangling symlinks
        self.fixSymlink(fname, target)
        
        # Move subs if any
        self.processSubs(fname, source, target)
        
    def fixSymlink(self, fname, target):
        if fname in os.listdir(self.SortConfig.ClutterDir):
            symlinkFile = os.path.join(self.SortConfig.ClutterDir, fname)
            
            if os.path.islink(symlinkFile):
                # Oh no, we need to fix this
                os.unlink(symlinkFile)
                target = os.path.join(target, fname)
                SortingEngine.symlink(symlinkFile, target)
                cprint('Fixed symlink ' + symlinkFile, 'red')
    
    def processMovieFile(self, fname):
        ''' Make a directory for orphan .AVIs and fix symlinks'''
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
        target = os.path.join(self.SortConfig.MoviesDir, dname)
        if not os.path.exists(target):
            os.mkdir(target)
        
        # Move file to directory
        source = os.path.join(self.SortConfig.MoviesDir, fname)
        shutil.move(source, target)
        print('Moved ',fname, 'to ', target)
        
        for subExt in self.SortConfig.SubsExtensions:
            subFname = os.path.splitext(fname)[0] + subExt
            
        # Move subtitle to the Movies folder
        if os.path.exists(subFname):
            source = os.path.join(self.SortConfig.MoviesDir, subFname)
            shutil.move(source, target)
            print('Moved', subFname, 'to', target)
        
        # Fix possible dangling symlinks
        self.fixSymlink(fname, target)
    
    def moveEpisodeDir(self, dname, possibleShowName):
        source = os.path.join(self.SortConfig.TvDir, dname)
        target = os.path.join(self.SortConfig.TvDir, possibleShowName)
        shutil.move(source, target)
        cprint('Moved ' + dname + ' to ' + target, 'red')
        
        self.fixSymlink(dname, target)
    
    def processTvDir(self, dname):
        guessedInfoDict = guessFileInfo(dname)
        
        if (guessedInfoDict['type'] == 'unknown'):
            return # This is a series folder, just skip it
        
        if self.SortConfig.Debug:
            print('Guessed TV ep info:', guessedInfoDict)
        
        availableShowDirs = os.listdir(self.SortConfig.TvDir)
        
        possibleShowName = None
        if 'series' in guessedInfoDict:
            possibleShowName = guessedInfoDict['series']
            
            if possibleShowName in availableShowDirs:
                self.moveEpisodeDir(dname, possibleShowName)
                return
                    
            if 'year' in guessedInfoDict:
                possibleShowName = possibleShowName + ' ' + str(guessedInfoDict['year'])
                
                self.moveEpisodeDir(dname, possibleShowName)
                return
        
            # A new show folder? Oh, joy!
            if possibleShowName:
                target = os.path.join(self.SortConfig.TvDir, possibleShowName)
                os.mkdir(target)
                self.moveEpisodeDir(dname, possibleShowName)
             
    def processMovieDir(self, dname):
        ''' 
        Un-archive files, make nice 
        '''
        crtDir = self.SortConfig.MoviesDir + os.sep + dname
        if self.SortConfig.Debug:
            cprint('Processing ' + crtDir, 'green')
        
        # Search for rar files
        targetPattern = re.escape(crtDir) + os.sep + '*.rar'
        if self.SortConfig.Debug:
            print('Pattern: ', targetPattern)
        
        cleanPattern = re.escape(crtDir) + os.sep + '*.r[0-9][0-9]'
        for rarfilename in glob.glob(targetPattern):
            if rarfile.is_rarfile(rarfilename):
                print('Found rarfile', rarfilename)
                print('Extracting ...',)
                # extract
                rarfile = rarfile.RarFile(rarfilename)
                rarfile.extractall(crtDir)
                print('done!')
                print('Deleting ', rarfilename)
                os.remove(rarfilename)
                
        # Delete all .rXX files
        for rarfilename in glob.glob(cleanPattern):
                # delete
                print('Deleting ', rarfilename)
                os.remove(rarfilename)
        
        # Process subs if they exists        
        subsDir = crtDir + os.sep + 'Subs'
        if (os.path.exists(subsDir)):
            # Need to process subs as well
            print('Processing subtitles dir')
            subsRarPattern = re.escape(subsDir) + os.sep + '*.rar'
            for subsRarfilename in glob.glob(subsRarPattern):
                # Extract subtitles
                if rarfile.is_rarfile(subsRarfilename):
                    print('Extracting ', subsRarfilename, '...', end=' ')
                    subsRarfile = rarfile.RarFile(subsRarfilename)
                    subsRarfile.extractall(crtDir)
                    print('done!')
                    #Remove it
                    print('Deleting ', subsRarfilename)
                    os.remove(subsRarfilename)
                    
                    # Extract idx if it exists
                    for idxRarfilename in glob.glob(subsRarfilename):
                        if rarfile.is_rarfile(idxRarfilename):
                            print('Extracting ', idxRarfilename, '...', end=' ')
                            idxRarfile = rarfile.RarFile(idxRarfilename)
                            idxRarfile.extractall(crtDir)
                            print('done!')
                            # Remove it
                            os.remove(idxRarfilename)
            
            # Delete subs dir
            print('Deleting ', subsDir)
            shutil.rmtree(subsDir)
        
