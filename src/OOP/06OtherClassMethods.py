#!/usr/bin/env python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
6. 本节内容主要讲究新式类中的一些重要的成员函数的使用方法

6.1 __str__
（1）一个类A，如果定义了__str__方法，那么打印A的实例时（print A），会直接调用其其__str__方法；
（2）若类A未定义__str__方法，那么打印A的实例时，结果是这个实例的地址；
（3）参见Example_06_01

6.2 __hash__
（1）用于定义一个对象的 hash code；
（2）对于不可变对象或序列，它们是可哈希的，直接调用这些对象的__hash__方法（或者hash('abc')），可以返回该对象的哈希值；
（3）另外，也可以自定义__hash__方法，由我们自己生成对象的 hash code；

-------------------------------------------------------------------------------------------------------------'''
# Example_06_01
class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
#     def __str__(self):
#         return self.first_name + self.last_name
    
p = Person('Liu', 'Fei', 30)
print p

# Example_06_02
print 'abc'.__hash__()      # 对于不可变对象，可直接调用其__hash__方法，返回它hash code；
print hash((1,2))           # 可是使用内建函数 hash()，达到同样的作用；