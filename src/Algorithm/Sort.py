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
'''

'''-----------------------------------------------------------------------------------------
1.各种排序算法性能分析
（1）时间复杂度比较
        名称                 平均速度         最坏情况
        冒泡排序法     O(n^2)     O(n^2)
        快速排序法     O(nlogn)   O(n^2)
        选择排序         O(n^2)     O(n^2)
        堆排序             O(nlogn)   O(nlogn)
        插入排序         O(n^2)     O(n^2)
        希尔排序         O(n^3/2)   O(n^2)
        归并排序         O(nlogn)   O(nlogn)
（2）稳定性
        冒泡、插入、归并三种方法稳定性较好，其余稍逊。
（3）空间复杂度
        上述各个方法中，除了归并排序，只需要使用1个元素的临时存储单元，用于交换数据；
        归并排序则需要n个元素的存储单元，用来保存多遍合并操作；
2.排序算法的选择
没有哪一种排序方法是全面胜出的，只有根据具体具体情况选择了。一般下面的原则可以考虑： 
（1）当数据为正序时，尽可能用冒泡、插入、快速方法
（2）如果n值较小（不超过50，但也要根据硬件状况确定），可以采用插入、选择排序。插入排序对小数量较为适用;
（3）如果n值较大，采用时间O(nlogn)的排序方法较适宜;
（4）如果强调稳定性，则使用归并排序。
-----------------------------------------------------------------------------------------'''

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
            # 在第 i 轮比较中，一共有 size-i 个元素需要进行比较，之间比较 size-i-1 次。
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

    def quick_sort(self, arr, left, right):
        '''
        @summary: 快速排序算法（V0.1：过程中不新建列表）
        @param arr: 待排序的列表
        @param left: 列表左边界下标
        @param right: 列表右边界下标
        @return: 排序之后的列表
        '''
        if (left < right):
            pivot = arr[left]
            low = left
            high = right
            while low < high:
                while low<high and arr[high]>=pivot:
                    high -= 1
                arr[low] = arr[high]
                while low<high and arr[low]<pivot:
                    low += 1
                arr[high] = arr[low]
            arr[low] = pivot
            self.quick_sort(arr, left, low-1)
            self.quick_sort(arr, low+1, right)
        return arr
    
    def quick_sort_1(self, arr):
        '''
        @summary: 快速排序算法（V0.2：过程中新建列表，采用Python特性实现）
        @param init_arr: 待排序的列表
        @return: 排序之后的列表
        '''
        if not arr:
            return []
        pivot = arr[0]
        less = self.quick_sort_1([x for x in arr[1:] if x<pivot])
        great = self.quick_sort_1([x for x in arr[1:] if x>=pivot])
        return less + [pivot] + great
            
    def shell_sort(self, arr):
        '''
        @summary: 希尔排序算法
        @todo: 暂时未弄明白
        '''
        size = len(arr)
        d = len(arr)/2
        while(d>=1):
            for i in range(d,size):
                tmp = arr[i]
                pos = i
                for j in range(i-d,-1,-d):
                    if arr[j] > tmp:
                        arr[j+d] = arr[j]
                        pos = j
                arr[pos]=tmp
            d = d/2  
        return arr

if __name__=="__main__":
    sort = Sort()
    init_arr = getrandata(10)
    print 'Before: %s' % init_arr
#     final_arr = sort.bubble_sort(init_arr)
#     final_arr = sort.select_sort(init_arr)
#     final_arr = sort.insert_sort(init_arr)
#     final_arr = sort.quick_sort(init_arr, 0, len(init_arr)-1)
#     final_arr = sort.quick_sort_1(init_arr)
    final_arr = sort.shell_sort(init_arr)
    print 'After: %s' % final_arr