# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 17:19:58 2022

@author: Trent

Code adapted from: https://stackabuse.com/radix-sort-in-python/
"""

from time import perf_counter

class RadixSort():
    def __init__(self):
        self.timing = None
        self.sorted = []
        self.timing_results = []

        # Private attributes used for final time elapsed calculation
        self.__start = None
        self.__stop = None
                
    # Private function used in sort
    def __countingSortForRadix(self, inputArray, placeValue):
        # We can assume that the number of digits used to represent
        # all numbers on the placeValue position is not grater than 10
        countArray = [0] * 10
        inputSize = len(inputArray)
    
        # placeElement is the value of the current place value
        # of the current element, e.g. if the current element is
        # 123, and the place value is 10, the placeElement is
        # equal to 2
        for i in range(inputSize):
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] += 1
    
        for i in range(1, 10):
            countArray[i] += countArray[i-1]
    
        # Reconstructing the output array
        outputArray = [0] * inputSize
        i = inputSize - 1
        while i >= 0:
            currentEl = inputArray[i]
            placeElement = (inputArray[i] // placeValue) % 10
            countArray[placeElement] -= 1
            newPosition = countArray[placeElement]
            outputArray[newPosition] = currentEl
            i -= 1
            
        return outputArray
    
    def sort(self, listToSort):
        self.__start = perf_counter()
        
        # Step 1 -> Find the maximum element in the input array
        maxEl = max(listToSort)

        # Step 2 -> Find the number of digits in the `max` element
        D = 1
        while maxEl > 0:
            maxEl /= 10
            D += 1
            
        # Step 3 -> Initialize the place value to the least significant place
        placeVal = 1

        # Step 4
        outputArray = listToSort
        
        # Recursively call counting sort
        while D > 0:
            outputArray = RadixSort.__countingSortForRadix(self, outputArray, placeVal)
            placeVal *= 10
            D -= 1
            
        self.sorted = outputArray
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
        
        return outputArray
    
