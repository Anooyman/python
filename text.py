#coding:utf-8
import socket
import struct
if __name__ == '__main__':
    #ip = socket.inet_ntoa(struct.pack('I',socket.htonl(int_ip)))
    ip = '127.0.0.1'
    int_ip = socket.ntohl(struct.unpack("I",socket.inet_aton(str(ip)))[0])
    int_ip = int_ip+1
    ip_ip = socket.inet_ntoa(struct.pack('I',socket.htonl(int_ip)))
    print int_ip
    print ip_ip 
