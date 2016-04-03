#coding:utf-8
import sqlite3

def creatdb():
    cx = sqlite3.connect("/home/anooy/python/test.db")
    cx.execute('''CREATE TABLE PACKETS
            ();''')

if __name__ == '__main__':
