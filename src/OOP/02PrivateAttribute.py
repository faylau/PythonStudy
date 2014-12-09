#encoding:utf-8
#!/usr/bin/python

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"


'''-------------------------------------------------------------------------------------------------------------
2.1访问控制（公有私有属性：01ClassAndObject_Example2.1）
（1）Python没有public/private/protect等访问权限控制的关键字（与Java不同）；
（2）Python通过在类属性前加“__”（双下划线）的方法，将类属性标识为私有属性；
（3）但上述方法只是一种“伪私有”，可以通过“_className__attrName”作为变量名进行访问（针对私有成员变量、私有成员方法都有效）。
-------------------------------------------------------------------------------------------------------------'''

class Parent(object):
    '''
    @summary: 01ClassAndObject_Example2.1
    '''
    a = 100         # 公有的静态变量
    __a = 200       # 私有的静态变量
    
    def func(self):
        print "Public function 'func'."
        print self.a            # 可以实例方法中访问公有变量
        print self.__a          # 不能在实例方法中访问私有变量
        print Parent.__a        # 可以在类内部（实例方法中）访问私有变量（此处通过ClassName.PrivateAttribute的方式访问）
        
    def __func(self):
        '''
        @summary: 私有的成员方法，无法在类外部访问。
        '''
        print "Private function '__func'."
        print self.a
        print self.__a
        
if __name__ == "__main__":

    # 01ClassAndObject_Example2.1------------------------------------------------------------------
    print Parent._Parent__a     # Parent类中私有变量 __a，实际上被转换成为变量 _Parent__a 提供访问。
    p = Parent()
    p.func()
    p.__func()                  # 无法在类外部访问private的方法
    p._Parent__func()           # 同上，类中的私有方法，实际上也可通过 instance._ClassName__func()的方式访问。