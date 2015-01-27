#!/usr/bin/env python
#encoding:utf-8

__authors__ = ['"Liu Fei" <liufei83@163.com>']
__version__ = "V0.1"

import contextlib

'''-------------------------------------------------------------------------------------------------------------
参考博文：http://python.jobbole.com/64175/

1. 上下文管理器是什么
（1）直接的解释，上下文管理器的任务是：代码块执行前准备，代码块执行后收拾；
（2）在Python2.5中加入，能够让代码可读性更强，错误更少；
（3）下面先介绍一个最简单的上下文管理器的例子（参见 Example_1.1）；
-------------------------------------------------------------------------------------------------------------'''
print "----------------Example_1.1----------------"
with open('Context.py', 'r') as f:
	print f.readline()	# 只读取第一行

'''-------------------------------------------------------------------------------------------------------------
2. 如何使用上下文管理器
2.1 首先来看，通常我们是如何打开一个文并写入“Hello World”的（Example_1.2）：
	* 先创建一个文件对象writer；
	* 写入内容；
	* 关闭文件对象；
（1）存在一个问题，若代码在写入或关闭文件对象前出错，那文件对象就无法回收了；
（2）比如，磁盘已满，在写入内容是出错；
（3）上述问题可以通过try-finally来解决，但在较复杂的代码中加入try-finally会变得很丑陋（暂时只能表面理解）；
2.2 我们可以选择使用上下文管理器来处理上述问题，请看Example_1.1中的例子：
（1）with 是一个关键词，并总伴随着上下文管理器出现；
（2）as 是另一个关键词，它表示将 open 函数返回的内容赋值给变量 f；
（3）接下来，在with语句块中就可以对文件对象f进行各种操作了；
（4）也就是，我们使用了“open”上下文管理器，它保证了代码既优雅又安全，出色地完成了try-finally的任务。
-------------------------------------------------------------------------------------------------------------'''
print "----------------Example_1.2----------------"
filename = 'test.txt'
writer = open(filename, 'w')
writer.write("Hello World")
writer.close()

'''-------------------------------------------------------------------------------------------------------------
3. 自定义上下文管理器
3.1 实现一个自定义的上下文管理器
（1）自定义一个上下文管理器，必须要实现两个方法：（Example_3.1）：
	* 一个负责进入语句块的操作：__enter__；
	* 一个负责离开语句块后的善后操作（即使遇到异常）：__exit__；
	* 说明：__exit__方法有3个参数，后面再谈。
（2）自定义一个“open”功能（文件操作）的上下文管理器：（Example_3.2）
	* 重写了__init__函数，接收了两个参数：filename和mode（文件名、打开文件模式）；
	* __enter__函数：执行语句块之前，通过__enter__函数打开一个文件，并返回文件对象；
	* __exit__函数：执行语句块之后（或中途遇到异常），通过__exit__函数关闭文件对象。
3.2 如何在上下文管理器中处理异常
（1）如果语句块内部发生异常，会调用__exit__方法来处理，异常将会被重新抛出；
（2）完整的__exit__方法是这样的：def __exit__(self, exc_type, exc_val, exc_tb):
	* exc_type：异常类型
	* exc_val：异常值
	* exc_tb：异常追踪信息
（3）举例（Example_3.3），__exit__方法只负责抛出SyntaxError异常。
-------------------------------------------------------------------------------------------------------------'''

print "----------------Example_3.1----------------"

class PypixContextManagerDemo(object):

	def __enter__(self):
		print 'Entering the block ......'

	def __exit__(self, *args):
		print 'Exiting the block ......'

with PypixContextManagerDemo():
	print 'In the block ......'

print "----------------Example_3.2----------------"

class PypixOpen(object):

	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode

	def __enter__(self):
		self.open_file = open(self.filename, self.mode)
		return self.open_file

	def __exit__(self, *args):
		self.open_file.close()

with PypixOpen('test.txt', 'a') as f:
	f.write("Hello World from a context-manager.")

print "----------------Example_3.3----------------"

class RaiseOnlyIfSyntaxError(object):

	def __enter__(self):
		pass

	def __exit__(self, exc_type, exc_val, exc_tb):
		return SyntaxError != exc_type

'''-------------------------------------------------------------------------------------------------------------
4. 一些关于上下文库（contextlib）的内容（参见博文：http://python.jobbole.com/64175/）
	contextlib是一个python模块，作用是提供更易用的上下文管理器
（1）contextlib.closing
	* 假设有一个创建数据库函数，它返回一个数据库对象，并在使用完毕后关闭相关资源（Example_4.1）；
（2）contextlib.nested
	* 假设有两个文件，一个读，一个写，进行拷贝，可使用contextlib.nested减少嵌套循环（Example_4.2）；
（3）contextlib.contextmanager
	* 对于python高级玩家来说，任何能够被yield关键字分割为两部分的函数，都能够通过上下文管理装饰器来实现；
	* 任何在yield之前的内容都可以看作在代码块执行前的操作（__enter__）；
	* 任何在yield之后的内容都可以看作在代码块执行后的操作（__exit__）；
-------------------------------------------------------------------------------------------------------------'''

print "----------------Example_4.1----------------"

# 假定CreateDataBase()存在，返回一个数据库连接对象。
class CreateDataBase(object):
	def close(self, *args):
		pass
	def query(self):
		pass
with contextlib.closing(CreateDataBase()) as db:
	db.query()

print "----------------Example_4.2----------------"

# old method
# with contextlib.nested(open('test.txt', 'r'), open('test1.txt', 'w')) as (reader, writer):
# 	writer.write(reader.read())

# new method in python 2.7
with open('test.txt', 'r') as reader, open('test1.txt', 'w') as writer:
	writer.write(reader.read())