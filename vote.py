#coding=utf-8

import sys,string
import struct
import socket

class VoteInfo :
    'Data class for vote information.'

    MAX_CANDIDATE = 1000
    MAX_WIRE_SIZE = 500
    
    MAGIC = 0x5400
    MAGIC_MASK = 0xFC00
    
    INQUIRY_FLAG = 0x0100
    RESPONSE_FLAG = 0x0200

    DELIMITER = '\n'
    DELI_SIZE = 2

    def __init__(self, candidate = -1, isInquiry = True, isResponse = False, count = 0):

        self.candidate = candidate
        self.isInquiry = isInquiry
        self.isResponse = isResponse
        self.count = count

    def setProperty(self, isInquiry, isResponse, count):

        self.isInquiry = isInquiry
        self.isResponse = isResponse
        self.count = count


    def printInfo(self):
        print 'VoteInfo:'
        print 'candidate: ',self.candidate
        print 'isInquiry: ',self.isInquiry
#        print 'isResponse',self.isResponse
        print 'now: ',self.count
#        print 'MAX_CANDIDATE: ', VoteInfo.MAX_CANDIDATE
#        print 'MAX_WIRE_SIZE: ', VoteInfo.MAX_WIRE_SIZE


    def encodeText(self):
        'Voting  <v|i> [R] <candidate ID> <count>'
        s = "Voting "
        if self.isInquiry:
            s += "i"
        else:
            s += "v"
          
        if self.isResponse:
            s += " R"

        if self.isResponse:
            return "{} {} {}".format(s, self.candidate, self.count)
        else:
            return "{} {}".format(s, self.candidate)


    def encodeBin(self):
        
        m = VoteInfo.MAGIC
        if self.isInquiry:
            m |= VoteInfo.INQUIRY_FLAG   # inquire flag
   
        if self.isResponse:
            m |= VoteInfo.RESPONSE_FLAG   # response flag

        if self.isResponse:
            return struct.pack("!hhq",m,self.candidate,self.count)
        else:
            return struct.pack("!hh",m,self.candidate)


    def decodeText(self, sText):
    
        txtlist = sText.split(' ')
        #print "decodeText: ", txtlist, len(txtlist)
        
        if len(txtlist) != 3 and len(txtlist) !=5 : return

        if txtlist[0] != "Voting": return

        if txtlist[1] == 'i': self.isInquiry = True
        elif txtlist[1] == 'v': self.isInquiry = False
        else: return

        if len(txtlist) == 5:
            if txtlist[2] == 'R':
                self.isResponse = True
                self.candidate = int(txtlist[3])
                self.count = int(txtlist[4])
            else: return 
        else: # len(txtlist) == 3:
            self.isResponse = False
            self.candidate = int(txtlist[2])
            

    def decodeBin(self, sText):
        #print "decodeBin......."
        length = len(sText)
        if length == 4:
            btuple = struct.unpack("!hh",sText)
            if (btuple[0] & VoteInfo.MAGIC_MASK != VoteInfo.MAGIC): return
        elif length == 12:
            btuple = struct.unpack("!hhq",sText)
            if (btuple[0] & VoteInfo.MAGIC_MASK != VoteInfo.MAGIC): return
            self.count = int(btuple[2])
        else: return

        self.isResponse = (btuple[0] & VoteInfo.RESPONSE_FLAG != 0)
        self.isInquiry = (btuple[0] & VoteInfo.INQUIRY_FLAG != 0)

        self.candidate = int(btuple[1])
            
    def getNextMsgText(self,sock):

        data = ''
        while True:
        
            s = sock.recv(1)
            if s == '':
                print "getNextMsgText: ", "stream closed by remote end."
                return -1
            elif s == VoteInfo.DELIMITER:
                break;
            else:
                data += s

        return data
        
    
    def getNextMsgBin(self,sock):
        #print "I'm here......."
        data = sock.recv(VoteInfo.DELI_SIZE)        
        length, = struct.unpack('!h',data)
        #print "I'm here.......", length
        return sock.recv(length)
    
            
    def putMsgText(self,data,sock):

        #find the delimter character in the data, just return
        #need byte stuffing
        if string.find(data,VoteInfo.DELIMITER) != -1 :
            return -1

        sock.sendall(data)
        sock.sendall(VoteInfo.DELIMITER)

        return len(data)+len(VoteInfo.DELIMITER)
    
    def putMsgBin(self,data,sock):

        if len(data) > 65535:
            print "putMsgBin: the data is too long, only two bytes for length"
            return -1
        #print "I'm here......."
        sock.sendall(struct.pack('!h',len(data)))
        #print "I'm here......."
        sock.sendall(data)
        #print "I'm here......."
        return len(data)+VoteInfo.DELI_SIZE

