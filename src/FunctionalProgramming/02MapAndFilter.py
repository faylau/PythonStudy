#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
2. map内建函数
2.1 map内建函数的定义与作用（Example_02）
（1）map(func, seq)
（2）参数func：一个具有特定功能的函数；参数seq：一个序列；
（3）map的作用：遍历seq中的每个元素，并将元素传递给func，然后将每次func返回的结果保存在一个list里面，作为最终的结果返回；
-------------------------------------------------------------------------------------------------------------'''
# Example_02_01
items = [1, 2, 3, 4, 5, 6]
def func(x):
    return x*x
print map(func, items)              # map的最基本用法
print map(lambda x: x*x, items)     # 第一个参数func也可以用lambda表达式替代
print [x*x for x in items]          # 这是一个比较pythonic的写法，等同于上面的 map 语句

'''-------------------------------------------------------------------------------------------------------------
3. filter内建函数
3.1 从字面意思理解，这个函数起到“过滤器”的作用；
3.2 filter的定义与作用（Example_03）
（1）filter(function, sequence)
（2）参数function：一个具有特定功能的函数，返回True或False；参数sequence：一个可迭代的序列；
（3）作用：遍历sequence中的每个元素并传递给function，把执行结果为True的元素放在一个List/String/Tuple（取决于sequence的类型）中返回；
-------------------------------------------------------------------------------------------------------------'''
# Example_02_02
items1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]        # filter可以接受不同类型的序列，包括list/tuple/dict/str等，返回的是同样类型的序列。
def func1(x):
    return x%2 == 0
print filter(func1, items1)                 # filter的最基本用法
print filter(lambda x: x%2==0, items1)      # 第一个参数func1也可以用lambda表达式替代
print [x for x in items1 if x%2==0]         # pythonic的写法，可以达到同样的效果。
print filter(lambda x: x!='c', 'abcde')     # filter同样可以接受str序列