#coding:utf-8

import sqlite3
import xml.etree.ElementTree as ET
import re

class Find_Value:
    def __init__(self,tree):
        self.tree = tree

    def find_value(self,kind,name):
        finder = []
        for item in self.tree.iter('proto'):
            for elem in item.iter('field'):
                if elem.attrib['name'] == kind:
                    finder.append(elem.attrib[ name ])
        return finder

    def find_seq(self):
        return self.find_value('tcp.seq','show')

    def find_sip(self):
        return self.find_value('ip.src','show')

    def find_dip(self):
        return self.find_value('ip.dst','show')

    def find_sport(self):
        return self.find_value('tcp.srcport','show')

    def find_dport(self):
        return self.find_value('tcp.dstport','show')

    def find_proto(self):
        return self.find_value('ip.proto','showname')

    def find_len(self):
        return self.find_value('len','value')

    def find_caplen(self):
        return self.find_value('caplen','value')

    def find_time(self):
        return self.find_value('timestamp','value')

class db:
    def __init__(self,db):
        self.db = db

    def build_db(self):
        connect = sqlite3.connect(self.db)
        connect.execute('''create table tcp
                (SEQ INT PRIMARY KEY, 
                 SIP INT,
                 DIP INT,
                 SPORT INT,
                 DPORT INT,
                 PROTO STRING,
                 LEN INT, 
                 TIME INT,
                 CAPLEN INT); ''')

    def insert(self,value):
        connect = sqlite3.connect(self.db)

    def find(self):
        connect = sqlite3.connect(self.db)

if __name__ == '__main__':
    tree = ET.parse("com.ophone.MiniPlayer.pdml") 
    value = Find_Value(tree) 
    db = db('tcp.db')

