#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
4. reduce内建函数
4.1 定义与作用（Example_04_02）：
（1）定义：def reduce(function, iterable, initializer=None)
（2）参数：function：一个特定功能的函数，用于对后面的迭代序列进行操作；
（3）参数：iterable：一个可迭代的序列；
（4）参数：initializer：一个初始值，缺省为None；若不为None，则最先进行它与序列第1个值的操作；
（5）作用：对序列进行迭代，将两个元素传递给function，将返回值作为第一个元素，将下序列迭代的下一个元素作为第二个元素一同传递给function；
4.2 reduce实例（Example_04_01）
4.3 酷例（Example_04_03）：计算 a[0]*b[0]+a[1]*b[1]+......
-------------------------------------------------------------------------------------------------------------'''
# Example_04_01
print reduce(lambda x, y: x+y, [1,2,3,4,5])     # reduce先计算1+2，然后将结果作为左值，与下一个迭代值3再次进行x+y操作，依此类推。
print reduce(lambda x, y: x+y, [1,2,3,4,5], 10) # 有一个初始值10，先进行10+x的操作，x初值为1，后续与前面一致。

# Example_04_02
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:    
            raise TypeError('reduce() of empty sequence with no initial value')    
    accum_value = initializer                                                                   
    for x in it:
        accum_value = function(accum_value, x)    
    return accum_value

# Example_04_03
# 最后来个很酷的例子，计算：a[0]*b[0]+a[1]*b[1]+......
a = [3,9,8,5,2]
b = [1,4,9,2,6]
print reduce(lambda x,y: x+y, map(lambda x,y: x*y, a, b))