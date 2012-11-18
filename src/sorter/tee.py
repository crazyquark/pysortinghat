'''
Created on Nov 18, 2012

@author: Cristian
'''

class Tee:
    '''
    Redirect stdout and stderr to log files, like tee in bash
    '''

    def __init__(self, fd1, fd2):
        '''
        Save file descriptors
        '''
        self.fd1 = fd1
        self.fd2 = fd2
        
    def write(self, text):
        '''
        Overwrite write method
        '''
        # Write to both file descriptors
        self.fd1.write(text)
        self.fd2.write(text)
        
    def flush(self):
        '''
        Overwrite flush
        '''
        self.fd1.flush()
        self.fd2.flush()
        
    def __del__(self):
        '''
        Close file descriptors when done
        '''
        self.fd1.close()
        self.fd2.close()