'''
Created on Sep 29, 2012

@author: Cristian Sandu
'''

import sys
import sorter


def main():
    print "The Sorting Hat is loading params"
    # if we have no params, the default values will be used
    if len(sys.argv) > 4:
        sorter.config.Config.ClutterDir = sys.argv[1]
        sorter.config.Config.MoviesDir = sys.argv[2]
        sorter.config.Config.TvDir = sys.argv[3]
    else:
        print '** No params specified, using default values **'
        print 'Usage: sort.py clutter_dir movies_dir tv_dir'

if __name__ == '__main__':
    main()




