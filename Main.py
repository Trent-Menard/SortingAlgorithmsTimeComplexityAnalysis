# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:59:27 2022

@author: Trent
"""
from BubbleSort import bubble_sort
# from QuickSort import quick_sort
from MergeSort import merge_sort
from RadixSort import radixSort

to_sort = [1,3,5,7,9,2,4,6,8,10]

print(bubble_sort(to_sort))
# print(quick_sort(to_sort)) Isnt't working.
print(merge_sort(to_sort))
print(radixSort(to_sort))
