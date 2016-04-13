#coding:utf-8

import sqlite3
import xml.etree.ElementTree as ET
import re

if __name__ == '__main__':
    tree = ET.parse("com.ophone.MiniPlayer.pdml") 
    root = tree.getroot()
    for item in tree.iter('proto'):
        for elem in item.iter('field'):
            print elem.attrib['name']

#    connect = sqlite3.connect("tcp.db") #    connect.execute('''CREATE TABLE TCP
#            (SEQ INT PRIMARY KEY,
#            SIP INT,
#            DIP INT,
#            SPORT INT,
#            DPORT INT,
#            PROTO STRING,
#            SIZE INT, 
#            TIME INT); ''')

