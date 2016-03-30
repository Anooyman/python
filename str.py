#coding:utf-8
import re
import string 
import types

#找到a中的所有数字
def find_number(a):
    return ''.join(re.findall(r'\d',a))
    
#计算字母频率创建字典(忽略大小写)
def make_dictionary(a):
    a=string.lower(a)       #将所有的英文字符变为小写
    wordlist=''.join(re.findall(r'[a-z]',a))
    dictionary={}
    for word in wordlist:
        dictionary[word] = dictionary.get(word,0)+1
    return dictionary

#创建字符串a的频率字典(忽略大小写)
def make_dictionary_withnum(a):
    a=string.lower(a)
    dictionary={}
    for word in a:
        dictionary[word] = dictionary.get(word,0)+1
    return dictionary


#去除除了第一个字符以外的重复字符
def rm_word(a):
    a=string.lower(a)
    wordlist=[]
    wordlist.append(a[0])
    for i in a:
        for j in wordlist:
            if i != j:
                n=1
            else:
                n=0
                break
        if n==1:
            wordlist.append(i)
    return wordlist

#对出现的字符进行排序，以list输出
def sort_dictionary(a):
    dictionary=make_dictionary(a)
    value=sorted(dictionary.iteritems(),key=lambda d:d[1],reverse=True)
    wordlist=[]
    n=0
    for i in value:
        wordlist.append(i[0])
    return wordlist

if __name__ == '__main__':
    a='aAsmr3idd4bgs7Dlsf9eAF'
    print '1.字符串包含数字：',find_number(a)
    print '2.频率统计：',make_dictionary(a)
    print '3.去重后字符串：',''.join(rm_word(a))
    print '4.出现频率最高的字符为：',sort_dictionary(a)

