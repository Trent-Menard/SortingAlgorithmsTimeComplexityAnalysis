# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:29:30 2022

@author: DJMack, Trent

Code adapted from: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""

from time import perf_counter

class BubbleSort():
    def __init__(self):
        self.timing = None
        self.sorted = []
        self.timing_results = []

        # Private attributes used for final time elapsed calculation
        self.__start = None
        self.__stop = None
        
    def sort(self, arr):
        self.__start = perf_counter()
        
        # Private nested funcntion used for swapping array elements
        def __swap(self, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)
        swapped = True
        
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if arr[i - 1] > arr[i]:
                    __swap(self, i - 1, i)
                    swapped = True
        self.sorted = arr
        
        self.__stop = perf_counter()
        self.timing = self.__stop - self.__start
        
        convenience_alias = None
                
        if len(self.sorted) == 1_000:
            convenience_alias = "1K"
        elif len(self.sorted) == 10_000:
            convenience_alias = "10K"
        elif len(self.sorted) == 100_000:
            convenience_alias = "100K"
            
        dictionary = {"test_" + convenience_alias if convenience_alias is not None else "test_" + str(len(self.sorted)):self.timing}
        self.timing_results.append(dictionary)
            
        return arr
