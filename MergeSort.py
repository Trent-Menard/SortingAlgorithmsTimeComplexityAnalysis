# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:29:59 2022

@author: DJMack, Trent

Code adapted from: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""
from time import perf_counter

class MergeSort():
    def __init__(self):
        
        self.timing = None
        self.sorted = []
        
        # Private attributes used for final time elapsed calculation
        self.__start = None
        self.__stop = None
        
    def sort(self, arr):
        self.__start = perf_counter()

        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        # Perform merge_sort recursively on both halves
        left, right = self.sort(arr[:mid]), self.sort(arr[mid:])

        # Merge each side together
        
        self.__stop = perf_counter()
        self.timing = self.__stop - self.__start
        
        return MergeSort.__merge(self, left, right, arr.copy())

    # Private function used for merging
    def __merge(self, left, right, merged):
        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):
          
            # Sort each one and place into the result
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor+right_cursor]=left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1
                
        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]
            
        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]
    
        self.sorted = merged
        
        return merged
