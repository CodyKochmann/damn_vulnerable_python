from os import popen

def bash(cmd):
    ''' subshells make things easy, so imma make em easier! '''
    return popen(cmd).read().strip().splitlines()
    
if __name__ == "__main__":
    for line in bash("chmod -R -v 777 ."):
        print(line)
