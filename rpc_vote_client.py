#coding: utf-8
#Created Time: 2016-05-11 10:38:08
import sys
import socket
import SimpleXMLRPCServer
import xmlrpclib

from vote import VoteInfo

def create():
    server = xmlrpclib.ServerProxy("http://localhost:5005")
    words = server.sayHello()

def vote_client(port,candidate,server_ip,way):

    server = xmlrpclib.ServerProxy("http://localhost:5005")
    v = VoteInfo(candidate,way)

    data = v.encodeText()
    if way:
        response = server.quiry(data)
    else:
        response = server.vote(data)

    v.decodeText(response)
    print 'Candidate:', v.candidate, ':', v.count

if __name__ == '__main__':
	way = sys.argv[1]
	candidate_ID = int(sys.argv[2])
	server_ip = sys.argv[3]
	if len(sys.argv) == 5:
		server_port = int(sys.argv[4])
	else:
		server_port = 5005

        if way == 'v':
            n = False
        else:
            n = True

        vote_client(server_port,candidate_ID,server_ip,n)


