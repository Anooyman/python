#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: SchoolMember.py
# ��������ʵ����ѧУ��Ա��

class SchoolMember:
	# ������,�������ı���
	sum_member = 0
	
	# __init__��������Ķ��󱻴���ʱִ��
	def __init__(self, name):
		self.name = name
		SchoolMember.sum_member += 1
		print "ѧУ�¼���һ����Ա��%s" % self.name
		print "�����г�Ա%d��" % SchoolMember.sum_member
	
	# ���ҽ���
	def say_hello(self):
		print "��Һã��ҽУ�%s" % self.name

	# __del__�����ڶ���ʹ�õ�ʱ������
	def __del__(self):
		SchoolMember.sum_member -= 1
		print "%s�뿪�ˣ�ѧУ����%d��" % (self.name, SchoolMember.sum_member)

# ��ʦ��̳�ѧУ��Ա��
class Teacher(SchoolMember):
	def __init__(self, name, salary):
		SchoolMember.__init__(self, name)
		self.salary = salary
	
	def say_hello(self):
		SchoolMember.say_hello(self)
		print "������ʦ���ҵĹ����ǣ�%d" % self.salary
	
	def __del__(self):
		SchoolMember.__del__(self)
# ѧ����
class Student(SchoolMember):
	def __init__(self, name, mark):
		SchoolMember.__init__(self, name)
		self.mark = mark
	
	def say_hello(self):
		SchoolMember.say_hello(self)
		print "����ѧ�����ҵĳɼ��ǣ�%d" % self.mark
	def __del__(self):
		SchoolMember.__del__(self)

t = Teacher("�ϻ�", 3000)
t.say_hello()
s = Student("С��", 77)
s.say_hello()