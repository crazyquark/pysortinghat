import os, sys

print('Setting up ss module')
# Add 'ss' module to our path
ss_path = os.path.abspath('../../ss')
sys.path.append(ss_path)

print('Sorter module reporting for duty!')
