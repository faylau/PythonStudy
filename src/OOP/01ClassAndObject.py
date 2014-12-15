#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
一、Python中的类与对象

1.1实例方法、类方法、静态方法（01ClassAndObject_Example1.1）
（1）实例方法
一般以self作为方法的第1个参数，必须与具体的对象（实例）绑定才能访问；
（2）类方法
一般以cls作为方法的第1个参数，cls表示类本身，定义时可使用@classmethod装饰器进行装饰；
（3）静态方法
不需要任何默认参数，定义方式与普通函数类似，可使用@staticmethod装饰器进行装饰；

1.2类方法与静态方法
（1）类方法既可通过类名调用，也可通过实例调用；静态方法也一样；
（2）定义类方法需要1个缺省参数cls；定义静态方法不需要任何缺省参数；
（3）父类中有1个静态方法，且子类没有重写，那么在子类中调用该方法时，实际上指向的还是父类中的方法；
（4）父类中有1个类方法，且子类没有重写，那么在子类中调用该方法时，实际上指向的是子类中（这是因为类方法中的缺省参数cls）；
（5）静态方法无法访问类属性或实例属性（其实跟类没什么关系）；类方法可以访问类变量，但无法访问实例变量。
-------------------------------------------------------------------------------------------------------------'''

class MethodTest(object):
    '''
    @summary: 01ClassAndObject_Example1.1
    '''
    count = 0
    def method_add(self):
        MethodTest.count += 1
        print "Instance method. Count is '%d'. My class is '%s'" % (self.count, self.__class__.__name__)
        
    @staticmethod
    def static_method_add():
        MethodTest.count += 1
        print "Static method. Count is '%d'." % MethodTest.count
        
    @classmethod
    def class_method_add(cls):
        MethodTest.count += 1
        print "Class method. Count is '%d'. %s" % (MethodTest.count, cls.__name__)
        
class SubMethodTest(MethodTest):
    '''
    '''
    pass

        
if __name__ == "__main__":
    # 01ClassAndObject_Example1.1------------------------------------------------------------------
    print "------------------01ClassAndObject_Example1.1------------------"
    # 调用实例方法（只能通过实例调用）
    mt = MethodTest()
    mt.method_add()
    # 调用静态方法（既可通过类名，也可通过实例调用）
    MethodTest.static_method_add()
    mt.static_method_add()
    # 调用类方法（既可通过类名，也可通过实例调用）
    MethodTest.class_method_add()
    mt.class_method_add()
    # 类方法与静态方法的区别（（3）和（4））
    smt = SubMethodTest()
    smt.static_method_add()
    smt.class_method_add()