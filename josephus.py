#coding:utf-8
import sys
    
if __name__  == '__main__':
    quitnum=int(sys.argv[2])
    allnum=int(sys.argv[1])
    print 'N =',allnum,'M =',quitnum,'退出序列为：',
    list1=[]
    for i in range(1,1+allnum):
        list1.append(i)
    quitnum=quitnum-1
    n=quitnum%allnum
    while len(list1) >= 1:
        print list1[n],
        del list1[n]
#最后的判断用于输出最后一个list参数，不用判断会报错
        if len(list1)==0:                
            break
        else:
            n=(n+quitnum) % len(list1)
