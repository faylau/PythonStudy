#!/usr/bin/env python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
6. 本节内容主要讲究新式类中的一些重要的成员函数的使用方法

6.1 __str__ [参见Example_06_01]
（1）一个类A，如果定义了__str__方法，那么打印A的实例时（print A），会直接调用其其__str__方法；
（2）若类A未定义__str__方法，那么打印A的实例时，结果是这个实例的地址；

6.2 __hash__ [参见Example_06_01、Example_06_02]
（1）用于定义一个对象的 hash code；
（2）对于不可变对象或序列，它们是可哈希的，直接调用这些对象的__hash__方法（或者hash('abc')），可以返回该对象的哈希值；
（3）另外，也可以自定义__hash__方法，由我们自己定义对象的 hash code生成方法；
（4）由此引申，可hash的对象可以作为dict的key，否则出错（此句话未真正理解透彻，目前试过的key可以使用数字、字符、元组）；

-------------------------------------------------------------------------------------------------------------'''
# Example_06_01
class Person(object):
    def __init__(self, first_name, last_name, age, sid):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sid = sid
        
    def __str__(self):
        '''
        @summary: 重写Person类的__str__方法，print该对象的实例时打印出该函数返回的内容。
        '''
        return self.first_name + self.last_name

    def __hash__(self):
        '''
        @summary: 重写Person类的 __hash__ 方法，使其返回哈希值为学号。
        '''
        return self.sid
        
    
p = Person('Liu', 'Fei', 30, '001')
print p
print p.__hash__()

# Example_06_02
print 'abc'.__hash__()      # 对于不可变对象，可直接调用其__hash__方法，返回它hash code；
print hash((1,2))           # 可是使用内建函数 hash()，达到同样的作用；
# print hash([1,2,3])         # 对于可变对象，调用hash()时出现Error：TypeError: unhashable type: 'list'

# Example_06_03
t = (1,2)
d = {t: "a"}
print d[t]

