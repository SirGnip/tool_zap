from xmlrpc.client import ServerProxy
server = ServerProxy("http://localhost:8551")
server.mytest(7)


