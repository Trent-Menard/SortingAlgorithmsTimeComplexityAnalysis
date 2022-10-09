# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 21:25:50 2022

@author: Ryan Hasty
"""

from time import perf_counter


class QuickS():
    def __init__ (self, array, low, high, count=0):
        self.array = array
        self.low = low
        self.high = high
        self.count = count
        self.timing = None
        self.sorted = []
        
        # Private attributes used for final time elapsed calculation
        self.__start = None
        self.__stop = None
    
    def partition(self, array, low, high, count):
        
        # set pivot to be last element in array
        self.pivot = array[high]
        
        # if looking for best time complexity set count to 1
        if (count == 1):
            # choose the center element of the array
            self.pivot = array[high//2]
        
        # pointer for greater element
        i = low - 1
     
        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= self.pivot:
     
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
     
                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])
     
        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
     
        # Return the position from where partition is done
        return i + 1
        
    def quickSorting(self, array, low, high, count):
        self.__start = perf_counter()
        
        if low < high:
     
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            self.pi = self.partition(array, low, high,count)
     
            # Recursive call on the left of pivot
            self.quick(array, low, self.pi - 1)
     
            # Recursive call on the right of pivot
            self.quick(array, self.pi + 1, high)

        self.__stop = perf_counter()
        self.timing = self.__stop - self.__start