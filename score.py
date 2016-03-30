#coding:utf-8
import sys

#计算平均成绩，输入为一个list
def count(n):
    num = 0.0
    i=0
    while i<10:
        num = num+list1[i]
        i=i+1
    num = num-max(n)-min(n)
    num = num/(len(n)-3)
    return num 

if __name__ == '__main__':
    list1=[]
    i=1
    while i < 11:
        print "评委",i,"，请输入成绩（0-100）"
        num=float(raw_input())
        if num>0 and num<100:
            list1.append(num)
            i=i+1
        else:
            print '输入有问题，请重新输入：'
    print "去掉一个最高分",max(list1),"去掉一个最低分",min(list1),"，本选手的最后得分为",'%.1f'%count(list1),"分"


#为什么要加入sys模块？？？？argv有什么用？？？？
#输入应该写成一个单独函数
