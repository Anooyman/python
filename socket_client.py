#coding:utf-8
import socket

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9999
    s = socket.socket()
    s.connect((host,port))
    while 1:
        cmd = raw_input("Please input cmd:")
        s.sendall(cmd)
        data = s.recv(1024)
        print data
    s.close()
