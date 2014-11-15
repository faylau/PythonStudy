# encoding:utf-8
#!/usr/bin/python

__authors__ = ['"Liu Fei" <liufei82@163.com>']
__version__ = "V0.1"

'''
# ChangeLog:
#-------------------------------------------------------------------------------------------
# Version        Date                Desc                                            Author
#-------------------------------------------------------------------------------------------
# V0.1           2014/11/15          初始版本                                                                                                Liu Fei 
#-------------------------------------------------------------------------------------------
from _ctypes import Array
'''

import random

def getrandata(num):
    '''
    @summary: 随机生成0-100之间的数，组成列表。
    @param num: 需要生成的随机数个数
    @return: 返回生成的随机数列表
    '''
    a = []  
    i = 0  
    while i < num:  
        a.append(random.randint(0, 100))  
        i += 1  
    return a

class Sort(object):
    '''
    @summary: 各种常见的基本排序算法实现
    '''
    def __init__(self):
        '''
        @summary: 构造函数
        '''
        pass
    
    def bubble_sort(self, arr):
        '''
        @summary: 冒泡排序
        @note: 每趟比较将最大的元素交换到队列尾，第二趟比较至倒数第二个元素结束，依此类推（每次比较把最小元素交换到队列头，是一样的道理）。
        '''
        size = len(arr)
        # 有 n 个元素，一共需要比较 n-1 轮
        for i in range(1, size):
            # 在第 m 轮比较中，一共有 n-m 个元素需要进行比较，之间比较 n-m-1 次。
            for j in range(0, size-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def select_sort(self, arr):
        '''
        @summary: 选择排序
        @note: 每趟比较找出最小元素的下标，在每趟比较结束时，将其与当前队列第1个元素交换；第n趟比较从第n个元素开始，依此类推。
        @param arr: 排序之前的列表
        @return: 排序之后的列表
        '''
        size = len(arr)
        # 有n个元素，共需要进行n-1趟比较。
        for i in range(0, size-1):
            index = i
            for j in range(i+1, size):
                if arr[index] > arr[j]:
                    index = j
            arr[index], arr[i] = arr[i], arr[index]
        return arr
    
    def insert_sort(self, arr):
        '''
        @summary: 插入排序
        @note: 第一趟比较从第2个元素开始，将其与之前的元素逐一比较，并将其插入到合适的位置；第二趟比较从第3个元素开始，依此类推。
        @param arr: 原始列表
        @return: 排序之后的列表
        '''
        size = len(arr)
        for i in range(1, size):
            for j in range(0, i):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
                
            
if __name__=="__main__":
    sort = Sort()
    init_arr = getrandata(10)
    print 'Before: %s' % init_arr
#     final_arr = sort.bubble_sort(init_arr)
#     final_arr = sort.select_sort(init_arr)
    final_arr = sort.insert_sort(init_arr)
    print 'After: %s' % final_arr
    
        
        