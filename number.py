#coding:utf-8
import sys
import math
#寻找素数
def findnum(n):
    if n<=1:
        return False
    else:
        i=2
        while i<= math.sqrt(n):
            if n%i==0:
                return False
            else:
                i=i+1
        return True


if __name__ == '__main__':
    if len(sys.argv) == 1:
        num =10
    else:
        num=int(sys.argv[1])
    print '1-',num,'之间的素数有：'
    for i in range(num+1):
        if findnum(i):
            print i,
            

