import sys
import time
import socket
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

PORT = 8551


# Restrict to a particular path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


def run_server():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)  # get IP dynamically from hostname
    print(f'RPC server starting up on {server_ip}:{PORT}')

    with SimpleXMLRPCServer((server_ip, PORT), requestHandler=RequestHandler, allow_none=True) as server:
        server.register_introspection_functions()

        @server.register_function
        def mytest(ct):
            for x in range(ct):
                print('running mytest', x)
                time.sleep(0.5)
            print('done')

        # Run the server's main loop
        server.serve_forever()


if __name__ == '__main__':
    run_server()

