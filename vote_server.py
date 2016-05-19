#coding: utf-8
#Created Time: 2016-05-11 10:37:52

import sys
import socket

from vote import VoteInfo

host = 'localhost'
voting_count = [0 for x in xrange(VoteInfo.MAX_CANDIDATE)]

def vote_server(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    sock.bind(server_address)
    sock.listen(5)

    while True:
        print "Waiting for client request ......."
        client,address = sock.accept()
        try:
            v = VoteInfo()
            data = v.getNextMsgText(client)
            v.decodeText(data)
            if v.candidate >= 0 and v.candidate <= VoteInfo.MAX_CANDIDATE:
                if  not (v.isInquiry ):
                    voting_count[v.candidate] = voting_count[v.candidate] + 1

            v.setProperty(False,True,voting_count[v.candidate])

	    print "Client:",address[0],'vote for',v.printInfo()
            data = v.encodeText()
            v.putMsgText(data,client)
        except socket.errno,e:
            print "Socket error:",e 
        except Exception,e:
            print "Other error:",e
        finally:
            client.close()

    

if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 5005
    else:
        port = int(sys.argv[1])

    vote_server(port)
