import socket
import sys

import argparse
import binascii
from vote import VoteInfo

host = 'localhost'
voting_count = [0 for x in xrange(VoteInfo.MAX_CANDIDATE)]

def vote_server(port):
    """ A simple echo server """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print "Starting up echo server  on %s port %s" % server_address
    sock.bind(server_address)
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(5) 
    while True: 
        print "Waiting to receive message from client"
        client, address = sock.accept() 

        try:
            v = VoteInfo()
            #data = v.getNextMsgBin(client)
            #print "getNextMsgBin: ", binascii.hexlify(data)
            #v.decodeBin(data)
            
            data = v.getNextMsgText(client)
            print "getNextMsgText: ", data
            v.decodeText(data)

            v.printInfo()

            if v.candidate >= 0 and v.candidate <= VoteInfo.MAX_CANDIDATE:
                if not(v.isInquiry):
                    voting_count[v.candidate] += 1
                    
            print '#'*50
            
            v.setProperty(False, True, voting_count[v.candidate])
            v.printInfo()
            #data = v.encodeBin()
            #print "encodeBin: ",binascii.hexlify(data)
            #v.putMsgBin(data, client)

            data = v.encodeText()
            print "encodeText: ",data
            v.putMsgText(data, client)
            
        except socket.errno, e:
            print "Socket error: ", e
        except Exception, e:
            print "Other error: ", e
        finally:
            client.close() 
   
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.port

    vote_server(port)
    
    
    
    


