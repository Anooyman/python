#coding: utf-8
#Created Time: 2016-05-11 10:38:08
import sys
import socket

from vote import VoteInfo


def vote_client(port,candidate,server_ip,way):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address = (server_ip,port)
    sock.connect(server_address)

    try:
        v = VoteInfo(candidate,way)
        v.printInfo()

        data = v.encodeText()
        print "encodeText: ", data
        v.putMsgText(data,sock)

        print '#'*50
        data = v.getNextMsgText(sock)
        print "getNextMsgText: ",data
        v.decodeText(data)

        v.printInfo()

    except socket.errno,e:
        print "Socket error: %s" %str(e)
    except Exception,e:
        print "Other exception: %s" %str(e)
    finally:
        sock.close()
    



if __name__ == '__main__':
	way = sys.argv[1]
	candidate_ID = int(sys.argv[2])
	server_ip = sys.argv[3]
	if len(sys.argv) == 5:
		server_port = int(sys.argv[4])
	else:
		server_port = 5005
        vote_client(server_port,candidate_ID,server_ip,way)


