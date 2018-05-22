from os import popen

def bash(cmd):
    ''' subshells make things easy, so imma make em easier! '''
    return popen(cmd).read().strip().splitlines()
    
if __name__ == "__main__":
    try:
        # you can use it to iterate over a command
        for line in bash("chmod -R -v 777 ."):
            print(line)
        # or you can use it to watch a live session
        for line in bash("bash -c 'python -m SimpleHTTPServer 80 || python -m http.server 80'"):
            print('server log - %s' % (line,))
    except:
        exit("you might need to run this as root or with sudo")
