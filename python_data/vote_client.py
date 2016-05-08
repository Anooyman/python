#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 1
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import socket
import sys

import argparse,binascii

from vote import VoteInfo

host = 'localhost'

def vote_client(port,candidate,inq):
    """ A simple echo client """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print "Connecting to %s port %s" % server_address
    sock.connect(server_address)
    
    # Send data
    try:

        # Send data
        v = VoteInfo(candidate,inq)
        v.printInfo()
        
        #data = v.encodeBin()
        #print "encodeBin: ",binascii.hexlify(data)
        #v.putMsgBin(data, sock)
        
        data = v.encodeText()
        print "encodeText: ",data      
        v.putMsgText(data, sock)
        
        print '#'*50
        # Look for the response
        #data = v.getNextMsgBin(sock)
        #print "getNextMsgBin: ", binascii.hexlify(data)
        #v.decodeBin(data)
        data = v.getNextMsgText(sock)
        print "getNextMsgText: ", data
        v.decodeText(data)

        v.printInfo()
            
    except socket.errno, e:
        print "Socket error: %s" %str(e)
    except Exception, e:
        print "Other exception: %s" %str(e)
    finally:
        sock.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    parser.add_argument('--candidate', action="store", dest="candidate", type=int, required=True)
    parser.add_argument('--I', action="store", dest="inqury", type=int, required=True)
    given_args = parser.parse_args() 
    port = given_args.port
    candidate = given_args.candidate

    if given_args.inqury > 0: inq = True
    else: inq = False
    
    vote_client(port,candidate,inq)
