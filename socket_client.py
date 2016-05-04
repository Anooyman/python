#coding:utf-8
import socket
import sys


def echo_client(message,address,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (address, port)
    sock.connect(server_address)
    sock.sendall(message)
    amount_received = 0
    amount_expected = len(message)
    print "Sending %s bytes echo string to server ....."  % amount_expected
    data = sock.recv(128)
    amount_received += len(data)
    print "Receive %s bytes echo string from server:"  % len(data)
    print data
    sock.close



if __name__ == '__main__':
    message = sys.argv[1]
    address = sys.argv[2]
    port = int(sys.argv[3])
    echo_client(message,address,port)

