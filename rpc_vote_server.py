#coding: utf-8
#Created Time: 2016-05-11 10:37:52

import sys
import socket
import time
import SimpleXMLRPCServer


from vote import VoteInfo

host = 'localhost'
voting_count = [0 for x in xrange(VoteInfo.MAX_CANDIDATE)]

class MyObject(object):

    def vote(self, data):
        v = VoteInfo()
        global address
        v.decodeText(data)

        if v.candidate >= 0 and v.candidate <= VoteInfo.MAX_CANDIDATE:
            if not(v.isInquiry):
                voting_count[v.candidate] += 1

        if v.isInquiry == True:
            print 'Client:', address[0], 'inquery for Candidate:',v.candidate, 'now', voting_count[v.candidate]
        else:
            print 'Client:', address[0], 'vote for Candidate:', v.candidate,'now', voting_count[v.candidate]

        info = time.strftime("%Y年%m月%d日,%H:%M:%S", time.localtime(time.time())) + ' ' + address[0] + ' ' + str(address[1]) + ' candidate:' + str(v.candidate) + ' ' + str(voting_count[v.candidate])

        file = open('rpc_vote.txt', 'a')
        file.write(info + '\n')
        file.close()

        v.setProperty(False, True, voting_count[v.candidate])
        data = v.encodeText()
        return data

    def quiry(self, data):

        v = VoteInfo()
        global address
        v.decodeText(data)

        if v.candidate >= 0 and v.candidate <= VoteInfo.MAX_CANDIDATE:
            if not(v.isInquiry):
                voting_count[v.candidate] += 1
        if v.isInquiry == True:
            print 'Client:', address[0], 'inquery for Candidate:',v.candidate, 'now', voting_count[v.candidate]
            pass
        else:
            print 'Client:', address[0], 'vote for Candidate:', v.candidate,'now', voting_count[v.candidate]
        info = time.strftime("%Y年%m月%d日,%H:%M:%S", time.localtime(time.time())) + ' ' + address[0] + ' ' + str address[1]) + ' candidate:' + str(v.candidate) + ' ' + str(voting_count[v.candidate])

        file = open('rpc_vote.txt', 'a')
        file.write(info + '\n')
        file.close()

        v.setProperty(False, True, voting_count[v.candidate])

        data = v.encodeText()
        return data

if __name__ == '__main__':
    if len(sys.argv) == 1:
        port = 5005
    else:
        port = int(sys.argv[1])

    server = SimpleXMLRPCServer.SimpleXMLRPCServer((host,port))
    obj = MyObject()
    server.register_instance(obj)
    address = server.get_request()[1]
    server.serve_forever()

