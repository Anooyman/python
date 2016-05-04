#coding:utf-8
import sys
import socket


def scan_ports(host,start_port,end_port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    remote_ip = socket.gethostbyname(host)
    end_port += 1
    for port in range(start_port,end_port):
        try:
            sock.connect((remote_ip,port))
            print 'Port ' + str(port) + ' is open'
            sock.close()
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error:
            pass

if __name__ == '__main__':
#    start_IP = sys.argv[1]
#    end_IP = sys.argv[2]
    if len(sys.argv) == 1:
        start_port = 1
        end_port = 65535
    else:
        start_port = int(sys.argv[1])
        end_port = int(sys.argv[2])
    scan_ports('localhost',start_port,end_port)
