#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
4. super和self

4.1 super（参见博文《python super()》http://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html）
（1）super主要是为了不显示调用父类的方法，主要优势体现在多重继承上，使用super可以智能的帮我们调用父类方法（不用显示指定父类）；
（2）super并不是一个函数，而是一个类名，形如super(B, self)事实上调用了super类的初始化函数，产生了一个super对象；
（3）super类的初始化函数并没有做什么特殊操作，只是简单记录了类类型（B）和具体实例（self）；
（4）super(B, self).func 的调用，并不是调用当前类的父类的func函数；
（5）Python的多继承类是通过MRO的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数只被调用一次（如果每个类都使用super）；
（6）混用super类和非绑定的函数是一种危险行为，这可能导致应该被调用的父类函数没有被调用，或者一个父类函数被调用多次；
（7）super只在new-style类中有效。

4.2 MRO
（1）对于传统类而言，MRO算法为：从左至右，深度优先；
（2）对于新式类而言，MRO（C3MRO）算法为：深度优先，从左至右遍历基类；
补充（1）：深度优先，从左到右遍历基类，先遍历高level的，再遍历低level的，如果任何类在搜索中是重复的，只有最后一个出现的位置被保留，
其余会从MROlist中删除。也就是说类的共同的祖先只有在其所有的子类都已经被check之后才会check。
补充（2）：如Example4.1.1中的继承结构，C3MRO算法遍历的结果为：F E B (O) C (A) (O) D A O，最终为 FEBCDAO；
但有一点要注意的是，类的共同的祖先只有在其所有的子类都已经被check之后才会check（这点很重要！）

4.3 self
（1）self是一个对象，表示当前实例化的对象；
（2）self只在类的实例方法中有效（类方法需要cls，静态方法不需要任何缺省参数）；
（3）self不是python的关键字，可以用其他名称代替（但最好不要搞特殊）；
（4）self类似Java中的this；
-------------------------------------------------------------------------------------------------------------'''

'''-------------------------------------------------------------------------------------------------------------
Example 4.1.1：使用“父类名.方法”的形式调用父类方法时，在多继承情况下可能导致4.1中（6）中的情况出现。
（1）下面的例子中，各类之间的继承关系如下：
    object
    |    \
    |     A
    |    /|
    B   C D
     \ /  |
      E   |
       \  |
        \ |
         \|
          F
（2）类A和类D的初始化函数被重复调用了2次，这并不是我们所期望的结果！我们所期望的结果是最多只有类A的初始化函数被调用2次；
（3）正常情况下，如果使用super调用父类方法，则可避免（2）中存在的问题。
-------------------------------------------------------------------------------------------------------------'''
class A(object):
    def __init__(self):
        print "enter A"
        print "leave A"

class B(object):
    def __init__(self):
        print "enter B"
        print "leave B"

class C(A):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"

class D(A):
    def __init__(self):
        print "enter D"
        super(D, self).__init__()
        print "leave D"
        
class E(B, C):
    def __init__(self):
        print "enter E"
#         super(E, self).__init__()
        B.__init__(self)
        C.__init__(self)
        print "leave E"

class F(E, D):
    def __init__(self):
        print "enter F"
#         super(F, self).__init__()
        E.__init__(self)
        D.__init__(self)
        print "leave F"

if __name__=="__main__":
#     f = F()
    print F.mro()
    print E.mro()