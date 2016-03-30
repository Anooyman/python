#coding:utf-8
import sys
#递归计算斐波那契数列
def cout(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return cout( n-1 )+cout( n-2 )

#非递归计算斐波那契数列
def count(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        i=1
        f1=0
        f2=1
        while i < n:
            f3=f1+f2
            f1=f2
            f2=f3
            i=i+1
    return f3

if __name__ == '__main__':   #main函数开头
    if len(sys.argv) == 1:   #默认参数
        num=8
    else:
        num=int(sys.argv[1])  #获取命令行参数

    list1=[];
    for n in range( num ):
        list1.append(count(n))
    print list1
