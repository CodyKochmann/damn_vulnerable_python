from os import popen

def bash(cmd):
    ''' subshells make things easy, so imma make em easier! '''
    return popen(cmd).read().strip().splitlines()
    
