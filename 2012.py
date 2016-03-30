#coding:utf-8
import sys
import string
import re
#以how的方式打开以name为名字的文件
#read_all：全文直接读
#len：返回文件长度
#line：以行读出文件
def open_file(name,how):
    file_object=open(name)
    if how == 'read_all':
        return file_object.read()
    if how == 'len':
        return len(file_object.read())
    if how == 'line':
        line=[]
        for i in file_object.readlines():
            line.append(i)
        return line
        
#将输入的content写入以name为名字的文件中
def write_file(name,content):
    file_object=open(name,'w')
    file_object.write(content)
    file_object.close()

#将open_name内的内容写入到write_name中
def openandwrite_file(open_name,write_name):
    line=open_file(open_name,'line')
    if write_name == 'text1.txt':
        text=string.replace(''.join(line),'\n','')
        write_file(write_name,text)
    if write_name == 'text2.txt':
        text=string.replace(''.join(line),'2012','2015')
        write_file(write_name,text)

#用于找出name文件中的所有数字字符串
def find_number(name):
    line=open_file(name,'line')
    return re.findall(r'\d[0-9]*',''.join(line))


if __name__ == '__main__':
    file_name=sys.argv[1]
    all_the_text=open_file(file_name,'read_all')
    file_len=open_file(file_name,'len')
    openandwrite_file(file_name,'text1.txt')
    openandwrite_file(file_name,'text2.txt')
    print '1.',file_name,'文档内容为：'
    print all_the_text
    print '2.',file_name,'文件原始长度为：',file_len,'字节'
    print '3.去掉换行后的新文件为：text1.txt'
    print '4.替换掉的新文件为：text2.txt'
    print '5.数字字串有：',find_number(file_name)
