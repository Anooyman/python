#coding: utf-8
#Created Time: 2016-05-11 10:37:52

import sys
import socket
import SocketServer
import threading
import time


from vote import VoteInfo

host = 'localhost'
voting_count = [0 for x in xrange(VoteInfo.MAX_CANDIDATE)]

class MyTCPHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        v = VoteInfo()
        data = v.getNextMsgBin(self.request)
        cur_thread = threading.current_thread()
        print cur_thread.name,

        v.decodeBin(data)

        if v.candidate >= 0 and v.candidate <= VoteInfo.MAX_CANDIDATE:
            if not(v.isInquiry):
                voting_count[v.candidate] += 1
        if v.isInquiry == True:
            print 'Client:', self.client_address[0], 'inquery for Candidate:', v.candidate, 'now', voting_count[v.candidate]
        else:
            print 'Client:', self.client_address[0], 'vote for Candidate:', v.candidate, 'now', voting_count[v.candidate]
        v.setProperty(False, True, voting_count[v.candidate])
        data = v.encodeBin()
        v.putMsgBin(data, self.request)


        info = time.strftime("%Y年%m月%d日,%H:%M:%S", time.localtime(time.time())) + ' ' + str(self.client_address[
            0]) + ' ' + str(self.client_address[1]) + ' candidate:' + str(v.candidate) + ' ' + str(voting_count[v.candidate])

        file = open('socket_vote.txt', 'a')
        file.write(info + '\n')
        file.close()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


   

if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 5005
    else:
        port = int(sys.argv[1])

    server = ThreadedTCPServer((host,port),MyTCPHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start() 
    server.serve_forever()
