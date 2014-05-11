#!/usr/bin/python3
'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import sys

import sorter.config
import sorter.cleaner
import sorter.engine

from sorter.tee import Tee

from termcolor import cprint

def main():
    print("The Sorting Hat is loading params")
    # if we have no params, the default values will be used
    if len(sys.argv) >= 4:
        configs = sorter.config.Config(sys.argv[1], sys.argv[2], sys.argv[3])
        
        if len(sys.argv) > 4:
            # In case of lots of params, debug and fake it
            configs.Debug = True
            configs.DryRun = True
    else:
        cprint('Usage: sort.py clutter_dir movies_dir tv_dir', 'red')
        sys.exit(1)
        
    # Phase 1: sort movies and TV episodes and move them to target folders
    engine = sorter.engine.SortingEngine(configs)
    engine.sortAndMoveToTarget()
    
    # Phase 2: clean up movies dir
    cleaner = sorter.cleaner.Cleaner(configs)
    cleaner.cleanMoviesDir()
    
    # Phase 3: clean up TV episodes dir
    cleaner.cleanTvDir()

if __name__ == '__main__':
    # Redirect stdout
    stdoutsav = sys.stdout
    outputlog = open('output.log', 'w')
    sys.stdout = Tee(stdoutsav, outputlog)
    
    # Redirect stderr
    stderrsav = sys.stderr
    errorslog = open('errors.log', 'w')
    sys.stderr = Tee(stderrsav, errorslog)
    
    main()
    
    cprint ('All done!', 'green')
