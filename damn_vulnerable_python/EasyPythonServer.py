import socketserver
from threading import Thread

evil = eval

class EasyCodeTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        ''' this runs input python code sent from a socket and returns the result '''
        try:
            data = b''
            next_byte = lambda: self.request.recv(1)
            
            for i in iter(next_byte, b''):
                data = data + i
                
            self.request.sendall(
                repr(evil(data.decode())).encode()
            )
        except Exception: 
            # this function creates a lot of errors so
            # lets make things run nicely so we can
            # quiet the logs
            pass
            
def run_server(host='0.0.0.0', port=9999):
    server = socketserver.TCPServer(
        (host, port), 
        EasyCodeTCPHandler
    )
    print('starting server on port %s' % (port,))
    Thread(
        target=server.serve_forever,
        daemon=False
    ).start()

if __name__ == "__main__":
    run_server()
    
