# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:25:50 2022

@author: Ryan Hasty

Code adapted from: https://www.codingcreativo.it/en/python-quicksort/
"""

from time import perf_counter
from enum import IntEnum

class QuickS():
        
    class Case(IntEnum):
        BEST = 0
        AVERAGE = 1;
        WORST = 2
        
    def __init__ (self):
        self.timing = None
        self.sorted = []
        self.timing_results = []

        # Private attributes used for final time elapsed calculation
        self.__start = None
        self.__stop = None
    
    def sort(self, listToSort, Case):
        
        self.__start = perf_counter()
                
        self.sorted = QuickS.__quick_sort(self, listToSort, Case)
        
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
            
        return self.sorted;
    
    def __quick_sort(self, listToSort, Case):
        
        length = len(listToSort)
        
        if length <= 1:
            return listToSort
        
        if Case.BEST:
        # Best Case: N/2
        # Choose the center element
            pivot = listToSort.pop(len(listToSort) // 2)
        elif Case.AVERAGE:
            # Average cas:e N/10 instead of N/2
            pivot = listToSort.pop(len(listToSort) // 10)
        elif Case.WORST:
            # Worst Case: presorted array + arr[0] or arr[n] as pivot
            # Set pivot to be last element
            pivot = listToSort.pop(len(listToSort) - 1)
            
        high, low = [], []
        # Separate into 2 lists - elements smaller than and larger than pivot
        for number in listToSort:
            if number > pivot:
                high.append(number)
            else:
                low.append(number)
        # Recursive calls on sorted listed + pivot re-create it
        return QuickS.__quick_sort(self, low, Case) + [pivot] + QuickS.__quick_sort(self, high, Case)
