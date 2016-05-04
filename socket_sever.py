#coding:utf-8
import socket
import sys

host = 'localhost'

def echo_server(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    sock.bind(server_address)
    sock.listen(5)

    while True:
        print "Waiting for client connection ......."
        client,address = sock.accept()
        data = client.recv(128)
        if data:
            client.send(data)
            print "Receive %s bytes echo string from %s " % (len(data),address)
            print data
        client.close()
    sock.close()
    

if __name__ == '__main__':
    port = int(sys.argv[1])
    echo_server(port)
