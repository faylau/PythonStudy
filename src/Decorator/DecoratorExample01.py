#!/usr/bin/python
# encoding:utf-8


__authors__ = ['"Liu Fei" <liufei82@163.com>']
__version__ = "V0.1"

'''
# ChangeLog:
#-------------------------------------------------------------------------------------------
# Version        Date                Desc                                          Author
#-------------------------------------------------------------------------------------------
# V0.1           2014/11/19          初始版本                                                                                           Liu Fei 
#-------------------------------------------------------------------------------------------
'''

'''
1.关于Decorator，这里并没有做特别详细和深入的讲解，只是给了一些常规的Decorator用法；
2.具体Decorator的学习，可以参考文章 http://coolshell.cn/articles/11265.html；
3.Decorator的使用很广泛，建议在平时coding过程中思考，哪些操作可以通过Decorator的方式解决，积累经验。
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

def hello1(fn):
    def wrapper():
        print "Hello function '%s'." % fn.__name__
        fn()
        print "Goodbye function '%s'" % fn.__name__
    return wrapper

@hello1
def foo1():
    '''
    @summary: 打印一句话。
    '''
    print "I am function 'foo1'."
    
'''-------------------------------------------------------------------------------------------------------
Example-02：被装饰的函数有固定个数的参数（如 foo2(a, b)）
@note: （1）被装饰的函数 foo2(a, b) 带有固定个数的参数；
@note: （2）装饰器 hello(fn) 本身不带任何参数（严格上说只带有一个被装饰的function的名称）；
----------------------------------------------------------------------------------------------------------
1.说明：
（1）function的参数在装饰器中以 wrapper(*args, **kwargs) 的形式传递；
（2）关于function(*args, **kwargs)的意义请参阅这两个参数相关的说明；
（3）*args参数表示可以同时接收n个参数，这n个参数与tuple的形式传递给函数；
（4）*kwargs表示可以同时传n个key-value形式的参数，这n个key-value形式的参数以list形式传递给函数。
-------------------------------------------------------------------------------------------------------'''

def hello2(fn):
    def wrapper(a, b):
        print "Hello function '%s'." % fn.__name__
        print "Parameters are '%s' and '%s'." % (a, b)
        fn(a, b)
        print "Goodbye function '%s'." % fn.__name__
    return wrapper

@hello2
def foo2(a, b):
    print "Function 'foo2' parameters are '%s' and '%s'." % (a, b)

'''-------------------------------------------------------------------------------------------------------
Example-03：被装饰的函数带有不固定个数的参数
@note: （1）被装饰的函数 foo3(a, b) 带有2参数，foo3_1(a, b, c)带有3个参数；
@note: （2）装饰器 hello(fn)接受动态个数的参数；
----------------------------------------------------------------------------------------------------------
1.说明：
（1）function的不固定个数参数在装饰器中以 wrapper(*args, **kwargs) 的形式传递；
（2）*args参数表示可以同时接收n个参数，这n个参数与tuple的形式传递给函数；
（3）*kwargs表示可以同时传n个key-value形式的参数，这n个key-value形式的参数以list形式传递给函数。
-------------------------------------------------------------------------------------------------------'''

def hello3(fn):
    def wrapper(*args, **kwargs):
        print "Hello functiono '%s'." % fn.__name__
        fn(*args, **kwargs)
        print "Goodbye function '%s'." % fn.__name__
    return wrapper

@hello3
def foo3(a, b):
    print "Function 'foo3(%s, %s)' is called. Result is '%s'." % (a, b, a+b)

@hello3
def foo3_1(a, b, c):
    print "Function 'foo3_1(%s, %s, %s)' is called. Result is '%s'." % (a, b, c, a+b+c)
    
'''-------------------------------------------------------------------------------------------------------
Example-04：装饰器带参数
@note: （1）被装饰的函数 foo4(a) 带有1个参数，但调用该函数的时候不需要传参；
@note: （2）装饰器带hello4(arg)带有1个参数；
@note: （3）foo4(a)需要的参数由装饰器 hello4("xyz")中的参数来传递；
----------------------------------------------------------------------------------------------------------
1.说明：
（1）function的不固定个数参数在装饰器中以 wrapper(*args, **kwargs) 的形式传递；
（2）*args参数表示可以同时接收n个参数，这n个参数与tuple的形式传递给函数；
（3）*kwargs表示可以同时传n个key-value形式的参数，这n个key-value形式的参数以list形式传递给函数。
-------------------------------------------------------------------------------------------------------'''
def hello4(arg):
    def wrapper(fn):
        def _wrapper():
            print "Hello function '%s'." % fn.__name__
            fn(arg)
            print "Goodbye function '%s'." % fn.__name__
        return _wrapper
    return wrapper

@hello4("xyz")
def foo4(a):
    print "Function 'foo4(a)' is called. Parameter is '%s'." % a

'''-------------------------------------------------------------------------------------------------------
Example-05：以class作为装饰器参数
@note: （1）作为参数的class中带有Static Method，用于在装饰器中以cls.method的形式调用；
@note: （2）本质上与Example-04差不多。
----------------------------------------------------------------------------------------------------------
1.说明：
（1）
-------------------------------------------------------------------------------------------------------'''
class mylocker(object):
    def __init__(self):
        print "mylocker.__init__() called."
    
    @staticmethod
    def acquire():
        print "mylocker.acuire() called."
    
    @staticmethod
    def unlock(self):
        print "mylocker.unlock() called."
        
class lockerex(mylocker):
    @staticmethod
    def acquire():
        print "lockerex.acuire() called."
        
    @staticmethod
    def unlock():
        print "lockerex.unlock() called."
        
def decorator_locker(cls):
    '''
    @note: cls必须实现静态方法acquire和unlock
    '''
    def _deco(fn):
        def __deco(*args, **kwargs):
            print "Before '%s' called." % fn.__name__
            cls.acquire()
            fn(*args, **kwargs)
            cls.unlock()
            print "After '%s' called." % fn.__name__
        return __deco
    return _deco

@decorator_locker(lockerex)
def foo5():
    print "Function 'foo5()' is called."
    

if __name__ == '__main__':
    # foo1()
    # foo2(1, 2)
    # foo3(1, 2)
    # foo3_1(1, 2, 3)
    # foo4()
    foo5()