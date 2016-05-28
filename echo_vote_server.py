#coding: utf-8
#Created Time: 2016-05-11 10:37:52

import sys
import socket
import time
import asyncore


from vote import VoteInfo

host = 'localhost'
voting_count = [0 for x in xrange(VoteInfo.MAX_CANDIDATE)]

class EchoHandler(asyncore.dispatcher_with_send):

    def __init__(self, sock=None, map=None, address=None):
        self.address = address
        asyncore.dispatcher_with_send.__init__(self, sock, map)

    def handle_read(self):
        try:
            v = VoteInfo()
            data = v.getNextMsgBin(self)
            v.decodeBin(data)

            if v.candidate >= 0 and v.candidate <= VoteInfo.MAX_CANDIDATE:
                if not(v.isInquiry):
                    voting_count[v.candidate] += 1
                if v.isInquiry == True:
                    print 'Client:', self.address[0], 'inquery for Candidate:', v.candidate, 'now', voting_count[v.candidate]
                else:
                    print 'Client:', self.address[0], 'vote for Candidate:', v.candidate, 'now', voting_count[v.candidate]

            v.setProperty(False, True, voting_count[v.candidate])

            info = time.strftime("%Y年%m月%d日,%H:%M:%S", time.localtime(time.time())) + ' ' + str(self.address[0]) + ' ' + str(self.address[1]) + ' candidate-' + str(v.candidate) + ' ' + str(voting_count[v.candidate])

            file = open('echo_vote.txt', 'a')
            file.write(info + '\n')
            file.close()

            data = v.encodeBin()
            v.putMsgBin(data, self)

        except socket.errno, e:
            print "Socket error: ", e
        except Exception, e:
            print "Other error: ", e
        finally:
            self.close()

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            Client, address = pair
            print 'Incoming connection from %s' % repr(address)
            handler = EchoHandler(sock=Client, address=address)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 5005
    else:
        port = int(sys.argv[1])

    server = EchoServer(host,port)
    asyncore.loop()

