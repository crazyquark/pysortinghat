#!/usr/bin/python3	
'''	
Created  Sep 29, 2012

@author: Cristian Sandu
'''

import sys, subprocess, os

import sorter.config
import sorter.cleaner
import sorter.engine

from sorter.tee import Tee

from termcolor import cprint

def main():
    print("The Sorting Hat is loading params")
    # if we have no params, the default values will be used
    if len(sys.argv) >= 4:
        configs = sorter.config.Config(clutter = sys.argv[1], movies = sys.argv[2], tv = sys.argv[3])
        
        if len(sys.argv) > 4:
            # In case of lots of params, debug and fake it
            configs.Debug = True
            configs.DryRun = True
    else:
        cprint('Usage: sort.py clutter_dir movies_dir tv_dir', 'red')
        cprint('No params were passed, will use settings from config/sorter.ini', 'yellow')
        configs = sorter.config.Config()
    
    # Before fucking things up, attempt to stop transmission-daemon(will restart it after all is done)
    isRoot = (os.geteuid() == 0)
    retcode = subprocess.call(['service', 'transmission-daemon', 'stop'] if isRoot else ['sudo', 'service', 'transmission-daemon', 'stop'])
    
    transmissionWasRunning = (retcode == 0)
    if not transmissionWasRunning:
        cprint('Failed to stop transmission-daemon, was it running?', 'yellow')
    
    try:
        # Phase 1: sort movies and TV episodes and move them to target folders
        engine = sorter.engine.SortingEngine(configs)
        engine.sortAndMoveToTarget()
        
        # Phase 2: clean up movies dir
        cleaner = sorter.cleaner.Cleaner(configs)
        cleaner.cleanMoviesDir()
        
        # Phase 3: clean up TV episodes dir
        cleaner.cleanTvDir()
    except Exception as e:
        cprint('There was an error: ' + e.message, 'yellow')
        retcode = 1
    finally:
        # Restart transmission if we stopped it
        if transmissionWasRunning:
            retcode = subprocess.call(['service', 'transmission-daemon', 'start'] if isRoot else ['sudo', 'service', 'transmission-daemon', 'start']) 
            if retcode != 0:
                cprint('Failed to restart transmission-daemon, not sure what happened, sorry...', 'yellow')
            sys.exit(retcode)
            
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
