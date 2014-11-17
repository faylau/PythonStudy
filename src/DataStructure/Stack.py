#!/usr/bin/python
# encoding:utf-8


__authors__ = ['"Liu Fei" <liufei82@163.com>']
__version__ = "V0.1"

'''
# ChangeLog:
#-------------------------------------------------------------------------------------------
# Version        Date                Desc                                          Author
#-------------------------------------------------------------------------------------------
# V0.1           2014/11/17          初始版本                                                                                            Liu Fei 
#-------------------------------------------------------------------------------------------
'''

class Stack(object):
    '''
    @summary: Python实现的栈数据结构
    '''
    def __init__(self, max_size=20):
        '''
        @summary: 构造函数
        @param max_size: 栈的大小，缺省为20；
        @ivar stack: 栈的数据存储容器（列表）
        @ivar max_size: 栈的大小
        @ivar top: 栈顶指针（初始值为-1，表示栈为空）
        '''
        self.stack = []
        self.max_size = max_size
        self.top = -1
    
    def size(self):
        '''
        @summary: 返回当前栈中元素个数
        '''
        return self.top + 1
    
    def is_empty(self):
        '''
        @summary: 判断当前栈是否为空
        @return: True or False
        '''
        return self.top == -1
    
    def is_full(self):
        '''
        @summary: 判断当前栈是否已满
        @return: True or False
        '''
        return self.top == self.max_size - 1
    
    def push(self, item):
        '''
        @summary: 元素入栈操作
        '''
        if not self.is_full():
            self.stack.append(item)
            self.top += 1
        else:
            raise Exception("Stack is Full. Cannot push items any more.")
        
    def pop(self):
        '''
        @summary: 元素出栈操作
        @return: 出栈的元素 or 报异常
        '''
        if not self.is_empty():
            self.top -= 1
            return self.stack.pop()
        else:
            raise Exception("Stack is Empty. There is no item to pop.")
        
    def show(self):
        '''
        @summary: 显示当前栈中的内容
        '''
        print self.stack
            
if __name__=="__main__":
    s = Stack(5)
    for i in range(0,5):
        s.push(i)
        s.show()
        print s.size()
    while not s.is_empty():
        s.pop()
        s.show()
        print s.size()