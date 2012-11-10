'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import sys
import sorter.config
import sorter.cleaner

def main():
    print "The Sorting Hat is loading params"
    # if we have no params, the default values will be used
    configs = sorter.config.Config()
    if len(sys.argv) > 4:
        configs.ClutterDir = sys.argv[1]
        configs.MoviesDir = sys.argv[2]
        configs.TvDir = sys.argv[3]
    else:
        print '** No params specified, using default values **'
        print 'Usage: sort.py clutter_dir movies_dir tv_dir'
        
    # Phase 1: cleanup!
    cleaner = sorter.cleaner.Cleaner(configs)
    cleaner.clean()

if __name__ == '__main__':
    main()




