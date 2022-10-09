# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:25:50 2022

@author: Ryan Hasty
"""

from time import perf_counter

class QuickSort():
    def __init__ (self):
        
        self.timing = None
        self.sorted = []
        
        # Private attributes used for final time elapsed calculation
        self.__start = None
        self.__stop = None
        
    def sort(self, listToSort, optimizePivot=False):
        self.__start = perf_counter()
        
        
        self._low = min(listToSort)
        self._high = max(listToSort)
                
        if self._low < self._high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = QuickSort.__partition(self, listToSort, optimizePivot)
     
            # Recursive call on the left of pivot
            QuickSort.sort(self, listToSort, pi - 1)
     
            # Recursive call on the right of pivot
            QuickSort.sort(self, listToSort, pi + 1)
            
        self.__stop = perf_counter()
        self.timing = self.__stop - self.__start
        
        return self.sorted
    
    def __partition(self, listToSort, optimizePivot):
        
        # choose the center element of the array - Best case
        if optimizePivot:
            pivot = listToSort[self._high//2]
        else:
            # Set pivot to be last element in array - Worst case
            pivot = listToSort[self._high]

        # pointer for greater element
        i = self._low - 1
     
        # traverse through all elements
        # compare each element with pivot
        for j in range(self._low, self._high):
            if listToSort[j] <= pivot:
     
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
     
                # Swapping element at i with element at j
                (listToSort[i], listToSort[j]) = (listToSort[j], listToSort[i])
     
        # Swap the pivot element with the greater element specified by i
        (listToSort[i + 1], listToSort[self._high]) = (listToSort[self._high], listToSort[i + 1])
     
        # Return the position from where partition is done
        return i + 1
        
    # def quickSorting(self, array, optimizePivot):
    #     self.__start = perf_counter()
                
    #     if self._low < self._high:
    #         # Find pivot element such that
    #         # element smaller than pivot are on the left
    #         # element greater than pivot are on the right
    #         pi = self.partition(array, self._low, self._high, optimizePivot)
     
    #         # Recursive call on the left of pivot
    #         self(array, self._low, pi - 1)
     
    #         # Recursive call on the right of pivot            
    #         self(array, pi + 1, self._high)

    #     self.__stop = perf_counter()
    #     self.timing = self.__stop - self.__start
