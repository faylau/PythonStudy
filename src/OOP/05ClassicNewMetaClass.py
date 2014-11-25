#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
4. 经典类、新式类和元类

4.1 Classic class 和 New-Style class
（1）经典类可以没有父类，如 class A()；新式类必须有父类，且object为所有类的根基类；
（2）两种类的MRO机制不同（具体请参见04SuperAndSelf中的4.2部分，简要介绍了两种类的MRO机制）；
（3）如果经典类被作为父类，子类调用父类的构造函数（使用super方法）时会出错；
（4）经典类：p.__class__为<class __main__.P2 at 0xb68bd1dc>；type(p)为<type 'instance'>；
（5）新式类：p.__class__为<class '__main__.P'>；type(p)为<class '__main__.P'>。

4.2 MetaClass
4.2.1 首先推荐一篇关于Python MetaClass学习的文章，堪称一绝，《深刻理解Python中的元类（metaclass）》：http://blog.jobbole.com/21351/
4.2.2 类的本质：
（1）类也是对象（Example_4.2.1）；这个对象（类）自身拥有创建对象（类实例）的能力，而这就是为什么它是一个类的原因；
4.2.3 元类type
（2）type()是一个内建的元类（Example_4.2.2），通过type(ClassName)可以看到，一个class的类型是'type'；
（3）type可以像这样工作（Example_4.2.3）：type(类名, 父类的元组（针对继承的情况，可以为空）, 包含属性的字典（名称和值）)
（4）元类，就是用来创建类（对象）的“东西”（类），type就是一个元类（Python在背后用来创建所有类的元类）；
（5）Python中所有的东西都是对象（包括整数、字符串、函数、类），它们都是从一个类创建而来（type）（Example_4.2.4）；
4.2.4 __metaclass__属性
（1）如果定义一个类的时候为其定义了__metaclass__属性，那么，Python会用元类来创建这个类；
（2）如果这个类（包括其父类）没有定义__meta__class，Python最后会用内建元类type来创建这个类；
（3）通常，可以在__metaclass__中放置一些代码（创建类的东西，type或任何使用type或者type子类）；
4.2.5 自定义元类（Example_4.2.5）
（1）通过继承type，并重写__new__()实现；
4.2.6 总结
（1）元类作用的最浅显理解：拦截类的创建-->修改类-->返回定制后的类；
（2）元类最主要的作用是创建API，一个典型的例子是Django ORM：
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
说明：models.Model定义了__metaclass__，并且使用了一些魔法能够将你刚刚定义的简单的Person类转变成对数据库的一个复杂hook。

-------------------------------------------------------------------------------------------------------------'''
class ObjectCreator(object):
    pass
my_obj = ObjectCreator()

# Example_4.2.1
print my_obj                # 打印：<__main__.ObjectCreator object at 0x01F94110>

# Example_4.2.2
print type(ObjectCreator)   # <type 'type'>，说明Class的类型是type，而type()是一个元类，它可以创建类)。

# Example_4.2.3
# 通过 ‘type(类名, 父类的元组（针对继承的情况，可以为空）, 包含属性的字典（名称和值）)’方式创建一个类
Person = type('Person', (), {'name':'andy'})
print Person                # <class '__main__.MyClass'>，MyClass是一个类；
print Person()              # <__main__.MyClass object at 0x01F94630>，MyClass类的实例；
print Person().name         # andy，打印类的属性值（方法属性也可以用同样的方式定义）；

# Example_4.2.4
i = 10
print i.__class__           # <type 'int'>
print i.__class__.__class__ # <type 'type'>

# Example_4.2.5
class UpperAttrMetaclass(type):
    '''
    @summary: 定义一个元类UpperAttrMetaclass，用于创建建，并将创建的类的属性名称都改为大写形式。
    @note: 继承自type元类
    '''
    def __new__(cls, name, base, dct):
        '''
        @summary: 将不以“__”开头的类属性名称更改为大写字母；
        @param cls: 类本身的引用（此处表示Person）；
        @param name: 要创建的类（使用元类创建的类）名称；
        @param base: 指定要创建的类的父类（是一个元组）；
        @param dct: 要创建的类的属性（是一个字典）；
        @return: 返回一个实例（要创建的类的实例）
        '''
        print dct
        attrs = dict([(name.upper(), value) for name, value in dct.items() if not name.startswith('__')])
        return super(UpperAttrMetaclass, cls).__new__(cls, name, base, attrs)

p = UpperAttrMetaclass('cName',(), {'age':18})  # 创建了一个名为cName的类，其属性age为小写，并生成一个cName的实例p；
print hasattr(p, 'age')                         # False：虽然定义cName类的时候，属性age是小写，但使用UpperAttrMetaclass创建时将其改为大写
print hasattr(p, 'AGE')                         # True