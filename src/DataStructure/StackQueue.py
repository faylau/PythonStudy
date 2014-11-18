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
    @note: FILO
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

class Queue(object):
    '''
    @summary: Python实现的队列数据结构
    @note: FIFO
    '''
    def __init__(self, max_size=20):
        '''
        @summary: 构造函数
        '''
        self.queue = []
        self.max_size = max_size
        
    def size(self):
        '''
        @summary: 返回当前队列中的元素个数
        '''
        return len(self.queue)
    
    def is_empty(self):
        '''
        @summary: 判断队列是否为空
        '''
        return self.queue == []
    
    def is_full(self):
        '''
        @summary: 判断队列是否已满
        '''
        return self.size() == self.max_size
    
    def head(self):
        '''
        @summary: 获取队列的队首元素
        '''
        return self.queue[self.head]
    
    def tail(self):
        return self.queue[self.tail]
    
    def enqueue(self, item):
        '''
        @summary: 为队列添加一个元素（队尾）
        '''
        if self.is_full():
            raise Exception("Queue is full. Cannot add items anymore.")
        else:
            self.queue.append(item)
            
    def dequeue(self):
        '''
        @summary: 删除队列中的一个元素（队首，FIFO）
        '''
        if self.is_empty():
            raise Exception("Queue is empty. Cannot delete items anymore.")
        else:
            return self.queue.pop(0)
        
    def show(self):
        '''
        @summary: 显示队列中的元素
        '''
        print self.queue

if __name__=="__main__":
#     s = Stack(5)
#     for i in range(0,5):
#         s.push(i)
#         s.show()
#         print s.size()
#     while not s.is_empty():
#         s.pop()
#         s.show()
#         print s.size()

    q = Queue(5)
    for i in range(0,5):
        q.enqueue(i)
        q.show()
    while not q.is_empty():
        q.dequeue()
        q.show()