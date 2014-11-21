#!/usr/bin/python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

'''-------------------------------------------------------------------------------------------------------------
二、深入了解“生成器”
1.生成器的执行过程（请参见Example02和Example3）：
（1）生成一个generator看起来和调用一个函数相似，但其实执行过程是不同的；
（2）生成generator时，不会执行任何函数代码，而是直到对其调用next()时函数代码才会开始执行；
（3）每执行到一个yield语句时就会中断，返回一个迭代值（保存了当前代码执行的位置）；
（4）下次执行代码从当前yield语句的下一条语句开始继续执行；
（5）就像一个正常的函数，在执行过程中被yield语句中断了数次，每次中断都会通过yield返回当前的迭代值。
-------------------------------------------------------------------------------------------------------------
三、生成器的定义方法
1.像上面的例 子那样，通过在函数中使用yield关键字来定义一个生成器；
2.直接通过生成器表达式定义：(x*2 for x in range(10))
注意：生成器表达式与列表表达的区别：[x*2 for x in range(10)]
-------------------------------------------------------------------------------------------------------------
四、生成器的判断
1.isgeneratorfunction(foo())：判断函数foo()是否是一个“生成器函数”；
2.isgenerator(g)：判断g是否是一个“生成器对象”。
-------------------------------------------------------------------------------------------------------------
五、一些比较好的关于Generator的文章
1.提高你的Python: 解释‘yield’和‘Generators（生成器）’
（http://www.oschina.net/translate/improve-your-python-yield-and-generators-explained）
（1）generator是用来产生一系列值的
（2）yield则像是generator函数的返回结果
（3）yield唯一所做的另一件事就是保存一个generator函数的状态
（4）generator就是一个特殊类型的迭代器（iterator）
（5）和迭代器相似，我们可以通过使用next()来从generator中获取下一个值
（6） 通过隐式地调用next()来忽略一些值
2.Python函数式编程指南（四）：生成器
http://www.cnblogs.com/huxi/archive/2011/07/14/2106863.html
-------------------------------------------------------------------------------------------------------------'''

from itertools import islice

def my_generator():
	'''
	@summary: Example02：了解生成器的执行过程
	'''
	a = 0
	while True:
		if a%2 == 0:
			yield a
			print "test..."
		a += 1

def fibonacci():
	'''
	@summary: Example03：斐波那契数列
	'''
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b


if __name__=="__main__":
	
	# Example02_Run01
	mg = my_generator()
	# 打印返回的第1个迭代值，注意，不会打印“test...”
	print next(mg)
	print "Begin iterater by for statement..."
	for i in xrange(5):
		print next(mg)

	# Example03_Run01
	mg3 = fibonacci()
	print list(islice(mg3, 10))
	# Example03_Run02
	for num in mg3:
		if num > 100:
			break
		print num