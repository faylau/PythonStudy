#!/usr/bin/python
# encoding:utf-8


__authors__ = ['"Liu Fei" <liufei82@163.com>']
__version__ = "V0.1"

'''
# ChangeLog:
#-------------------------------------------------------------------------------------------
# Version        Date                Desc                                          Author
#-------------------------------------------------------------------------------------------
# V0.1           2014/11/19          初始版本                                                                                             Liu Fei 
#-------------------------------------------------------------------------------------------
'''

'''-------------------------------------------------------------------------------------------------------
Example-01：最基本的Decorator（装饰器）
@note: （1）被装饰的函数 foo1() 不带任何参数；
@note: （2）装饰器 hello(fn) 本身也不带任何参数（严格上说只带有一个被装饰的function的名称）。
----------------------------------------------------------------------------------------------------------
1.结合输出结果可以看到如下的东西：
（1）函数 foo1 前面有个 @hello 的“注解”，hello 就是我们前面定义的装饰器hello（由此可知装饰器其实就是一个函数）。
（2）在 hello 函数中，其需要一个 fn 的参数（这就用来做回调的函数）
（3）hello 函数中返回了一个 inner 函数 wrapper，这个 wrapper 函数回调了传进来的 fn，并在回调前后加了两条语句。

2.Decorator的本质：
（1）当你在用某个@decorator来修饰某个函数func时，其解释器会解释成下面这样的语句：    
    func = decorator(func)
（2）由下面的例子可以看到，hello(foo1)返回了wrapper()函数，所以，foo1其实变成了wrapper的一个变量，而后面的foo1()执行其实变成了wrapper()。
-------------------------------------------------------------------------------------------------------'''

def hello(fn):
    def wrapper():
        print "Hello function '%s'." % fn.__name__
        fn()
        print "Goodbye function '%s'" % fn.__name__
    return wrapper

@hello
def foo1():
    '''
    @summary: 打印一句话。
    '''
    print "I am function 'foo1'."
    
'''-------------------------------------------------------------------------------------------------------
Example-02：被装饰的函数有参数（如 foo2(a, b)）
@note: （1）被装饰的函数 foo1() 不带任何参数；
@note: （2）装饰器 hello(fn) 本身也不带任何参数（严格上说只带有一个被装饰的function的名称）。
----------------------------------------------------------------------------------------------------------
1.结合输出结果可以看到如下的东西：
（1）函数 foo1 前面有个 @hello 的“注解”，hello 就是我们前面定义的装饰器hello（由此可知装饰器其实就是一个函数）。
（2）在 hello 函数中，其需要一个 fn 的参数（这就用来做回调的函数）
（3）hello 函数中返回了一个 inner 函数 wrapper，这个 wrapper 函数回调了传进来的 fn，并在回调前后加了两条语句。
-------------------------------------------------------------------------------------------------------'''

def foo2(a, b):
    print 


if __name__ == '__main__':
    foo1()