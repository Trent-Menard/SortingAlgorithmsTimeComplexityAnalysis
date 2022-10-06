# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:59:27 2022

@author: Trent
"""

from BubbleSort import bubble_sort
# from QuickSort import quick_sort
from MergeSort import merge_sort
from RadixSort import radixSort

from ListGeneration import ListGeneration

from time import perf_counter
# READ: Quicksort isn't working rn. Either fix bug or find new alg.
# Code is messy & repetitive but I plan on making functions to clean it up later

# Use the same data set for each algorithm.
tst_lst = ListGeneration()

def printHeader():
    print(f'{"Size" : ^15} {"Time Elapsed" : ^15} {"Min" : ^15} {"Max" : ^10} {"Range" : ^15}')
    
def printSortHeader(sort, sortCase):
    print()
    print(f'{"" : ^24} Running {sort} Case for {sortCase} Sort')

def runRadixTest(listToSort):
    start = perf_counter()
    test_result = radixSort(listToSort)
    stop = perf_counter()
    print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {min(listToSort) : ^15} {max(listToSort) : ^10} {max(listToSort) - min(listToSort) : ^15}' )
    return test_result;

def runMergeTest(listToSort):
    start = perf_counter()
    test_result = merge_sort(listToSort)
    stop = perf_counter()
    print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {min(listToSort) : ^15} {max(listToSort) : ^10} {max(listToSort) - min(listToSort) : ^15}' )

    return test_result;

def runBubbleTest(listToSort):
    start = perf_counter()
    test_result = bubble_sort(listToSort)
    stop = perf_counter()
    print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {min(listToSort) : ^15} {max(listToSort) : ^10} {max(listToSort) - min(listToSort) : ^15}' )

    return test_result;

# Run each dataset for each sorting algorithm

# These tests could be combined in for loop but is 
# designed this way for propor formatting

# Test Radix sort BEST case (already sorted): Ω(n+k)
printSortHeader("BEST", "RADIX")
printHeader()
for x in tst_lst.cumulative_dataset_ascending:
    runRadixTest(x)

# Test Radix sort AVERAGE (random) case: θ(nk)
printSortHeader("AVERAGE", "RADIX")
printHeader()
for x in tst_lst.cumulative_dataset_random:
    runRadixTest(x)
    
# Test Radix sort WORST case O(nk):
printSortHeader("WORST", "RADIX")
printHeader()
for x in tst_lst.cumulative_dataset_descending:
    runRadixTest(x)
    
print("----------------------------------------------------------------------")
#Starting the Bubble Sort Test

printSortHeader("BEST", "BUBBLE")
printHeader()
for x in tst_lst.cumulative_dataset_ascending:
    runBubbleTest(x)

printSortHeader("AVERAGE", "BUBBLE")
printHeader()
for x in tst_lst.cumulative_dataset_random:
    runBubbleTest(x)

printSortHeader("WORST", "BUBBLE")
printHeader()
for x in tst_lst.cumulative_dataset_descending:
    runBubbleTest(x)
    
print("----------------------------------------------------------------------")
#Starting the Merge Sort Test

# Test Merge sort BEST case (already sorted): Ω(n log(n))
printSortHeader("BEST", "MERGE")
printHeader()
for x in tst_lst.cumulative_dataset_ascending:
    runMergeTest(x)

# Test Merge sort AVERAGE (random) case: θ(n log(n))
printSortHeader("AVERAGE", "MERGE")
printHeader()
for x in tst_lst.cumulative_dataset_random:
    runMergeTest(x)

# Test Merge sort WORST case O(n log(n)):
printSortHeader("WORST", "MERGE")
printHeader()
for x in tst_lst.cumulative_dataset_descending:
    runMergeTest(x)
