#coding:utf-8
class SchoolMember:
    sum_number=0
    def __init__(self,name):
        self.name=name
        SchoolMember.sum_number+=1
        print "学校新加入一个成员：",self.name
        print "现在有成员",SchoolMember.sum_number,"人"

    def say_hello(self):
        print "大家好，我叫：",self.name

    def __del__(self):
        SchoolMember.sum_number-=1
        print "%s离开了，学校还有%d人" % (self.name,SchoolMember.sum_number)

class Teacher(SchoolMember):
    def __init__(self,name,salary):
        SchoolMember.__init__(self,name)
        self.salary=salary
    
    def say_hello(self):
        SchoolMember.say_hello(self)
        print "我是老师，我的工资是：",self.salary

    def __del__(self):
        SchoolMember.__del__(self)

class Student(SchoolMember):
    def __init__(self,name,mark,idnum):
        SchoolMember.__init__(self,name)
        self.mark=mark
        self.idnum=idnum

    def say_hello(self):
        SchoolMember.say_hello(self)
        print "我是学生，我的成绩是：%d，我的学号是%d"%(self.mark,self.idnum)

    def __del__(self):
        SchoolMember.__del__(self)
if __name__ == '__main__':
    t=Teacher("老黄",3000)
    t.say_hello()
    s=Student("小河",77,2012001)
    s.say_hello()
