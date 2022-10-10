# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:25:50 2022

@author: Ryan Hasty
"""

from time import perf_counter

class QuickS():
    def __init__ (self):
        self.timing = None
        self.sorted = []
        self.timing_results = []

        # Private attributes used for final time elapsed calculation
        self.__start = None
        self.__stop = None
    
    def sort(self, listToSort, OptimizePivot=False):
        self.__start = perf_counter()
        
        res = QuickS.__quickSort(self, listToSort, 0, len(listToSort) - 1, OptimizePivot)
        
        self.sorted = res
                
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
    
    def __quickSort(self, listToSort, low, high, OptimizePivot=False):
        
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            self.pi = self.partition(listToSort, low, high, OptimizePivot)
     
            # Recursive call on the left of pivot
            
            QuickS.__quickSort(self, listToSort, low, self.pi - 1)
                 
            # Recursive call on the right of pivot
            QuickS.__quickSort(self, listToSort, self.pi + 1, high)
    
    def partition(self, listToSort, low, high, OptimizePivot):
        # Worst case : pivot is extreme (end or beginning) & pre-sorted (ascending) list
        
        # set pivot to be last element in listToSort
        pivot = listToSort[high]
        
        # choose the center element of the listToSort - Best case
        if OptimizePivot:
            pivot = listToSort[high//2]
        else:
            # Set pivot to be last element in listToSort - Worst case
            pivot = listToSort[high]
            
        # pointer for greater element
        i = low - 1
     
        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if listToSort[j] <= pivot:
     
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
     
                # Swapping element at i with element at j
                (listToSort[i], listToSort[j]) = (listToSort[j], listToSort[i])
     
        # Swap the pivot element with the greater element specified by i
        (listToSort[i + 1], listToSort[high]) = (listToSort[high], listToSort[i + 1])
     
        # Return the position from where partition is done
        return i + 1
