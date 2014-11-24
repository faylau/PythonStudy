#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
3.1构造函数和初始化
（1）Python中的__init__和__new__两个方法用于实例的构造和初始化；
（2）__init__是实例方法（以self作为第一个缺省参数），__new__则是一个类方法（以cls作为第一个缺省参数）；
（3）如果同时存在__init__和__new__，那么实例化时先运行__new__后运行__init（__new__是类自带的内建方法）；
（4）调用__init__不会返回任何值（None）；调用__new__返回一个实例，解释器会在__init__被调用前，将这个实例作为self传递过去；
（5）更通俗的说法：__new__是构造函数，__init__是初始化函数；
（6）这与Java不一样，个人理解，Java中的构造函数同时完成了上面两个函数的功能。
（7）通过重载__new__，可以实现很多功能（举例：单例模式Singleton）；

3.2一些特殊的实例属性
（1）C.__name__：类名
（2）C.__bases__：父类
（3）C.__dict__：类属性
（4）C.__module__：类所在的模块
（5）c.__class__：实例c所对应的类
-------------------------------------------------------------------------------------------------------------'''
class Parent(object):
    def __init__(self):
        print "Init a instance."
        
    def __new__(cls):
        print "New a instance."
        return super(Parent, cls).__new__(cls)
        
class Singleton(object):
    '''
    @summary: 通过自定义__new__实现单例模式
    '''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

if __name__=="__main__":
    # 创建一个实例时，缺省先运行__new__方法，打印"New a instance."。
    p1 = Parent()        
    
    # 单例模式下，创建的所有实例实际上都是同一个实例，通过id()可以看出来。
    s1 = Singleton()
    s2 = Singleton()
    print id(s1)
    print id(s2)