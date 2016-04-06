#coding:utf-8

import xml.dom.minidom
import sqlite3


if __name__ == '__main__':
#    DOMTree = xml.dom.minidom.parse("123.xml") #    collection = DOMTree.documentElement
#    proto = collection.getElementsByTagName("proto")
#    for item in proto:
#        if item.getAttribute("name") == "tcp":
#            print item.getAttribute("name")
#            print item.getAttribute("showname")
#            print item.getAttribute("size")

    connect = sqlite3.connect("tcp.db")
    connect.execute('''CREATE TABLE TCP
            SEQ INT PRIMARY KEY
            SIP INT
            DIP INT
            SSORT INT
            DSORT INT
            PROTO STRING
            SIZE INT 
            TIME INT ''')

