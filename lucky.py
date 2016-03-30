#coding:utf-8
import sys
import random
import time
import re
import select
import termios
import os 

#检测用户键盘输入函数，windows下无需这个函数，直接调用mscvrt模块
def kbhit():
    fd = sys.stdin.fileno()
    r = select.select([sys.stdin],[],[],0.01)
    rcode=''
    if len(r[0])>0:
        rcode = sys.stdin.read(1)
    return rcode

#创建名为“pool.txt”的文件，包含所有的电话号码
def creat_number():
    list1=[]
    for i in range(18829230000,18829239999):
        list1.append(str(i))
        write_file('pool.txt','\n'.join(list1))
    return list1

#将content写入name文件中
def write_file(name,content):
    file_object=open(name,'w')
    file_object.write(content)
    file_object.close()

#按行读取name文件内容
def read_file(name):
    file_object=open('pool.txt')
    line=[]
    for i in file_object.readlines():
        line.append(i)
    return line

#每100ms从file_name中随机选出一行，用回车键停止滚动
def find_number(file_name):
    while True:
        get_number=random.choice(read_file(file_name))
        print get_number
        time.sleep(0.1)
        c=kbhit()
        if len(c)!=0:
            if c in '\r\n':
                 break
    return get_number
 

if __name__ == '__main__':
    file_name=sys.argv[1]
    print "滚动开始（输入回车，滚动停止）："
    lucky_number=find_number(file_name)
    print '中奖的号码为：',lucky_number
      
               
              
      
      
