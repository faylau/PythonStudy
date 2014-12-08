#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
一、从一个简单的例子了解“生成器”的概念
1.生成器，用于“生成值的序列”；
2.定义生成器与普通函数的不同之处（请参见Example01）：
（1）普通函数要返回一个值的时候，使用return；
（2）生成器要生成一个值的时候，使用yield（注意，是“生成”而不是“返回”）；
（3）当函数的主体包含yield关键字时，它就成为了一个生成器；
3.生成器的一些特点（请参见Example01_run01和Example01_Run02）：
（1）“生成器”就是一类特殊的“迭代器”；作为一个“迭代器”，必须包含或定义一些方法，如__next__()；
（2）如同迭代器一样，可以使用next()函数来获取下一个值；其实next()调用的就是迭代器的__next__()方法；
（3）每当生成器被调用时，它会通过yield返回一个值给调用者（此“返回”不同于“return”）；
-------------------------------------------------------------------------------------------------------------'''
def simple_generator():
	'''
	@summary: Example01：第1个简单的生成器
	'''
	yield 1
	yield 2
	yield 3


if __name__=="__main__":
	# Example01_Run01
	print "------Example01_Run01-------"
	for value in simple_generator():
		print value

	# Example01_Run02
	my_generator = simple_generator()
	print next(my_generator)
	print next(my_generator)
	print next(my_generator)
	# 当无法继续迭代时（函数通过return返回数据，或者迭代到了生成器的末尾），抛出StopIteration异常。
	print next(my_generator)
