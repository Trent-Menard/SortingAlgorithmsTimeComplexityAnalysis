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

#    print(f'Size: {len(listToSort)} {"" : >5} Time Elapsed: {stop - start : .5f} {"Max" : >5}')

def printHeader():
    print(f'{"Size" : ^15} {"Time Elapsed" : ^15} {"Min" : ^15} {"Max" : ^15} {"Variance" : ^15}')
    
def printSortHeader(sort, sortCase):
    print()
    print(f'{"" : ^24} Running {sort} Case for {sortCase} Sort')

def runRadixTest(listToSort):
    start = perf_counter()
    test_result = radixSort(listToSort)
    stop = perf_counter()
    # print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {listToSort[0] : ^15} {listToSort[-1] : ^15} {listToSort[-1] - listToSort[0] : ^15}' )
    print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {"TBD" : ^15} {"TBD" : ^15} {"TBD" : ^15}' )
    return test_result;

def runMergeTest(listToSort):
    start = perf_counter()
    test_result = merge_sort(listToSort)
    stop = perf_counter()
    # print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {listToSort[0] : ^15} {listToSort[-1] : ^15} {listToSort[-1] - listToSort[0] : ^15}' )
    print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {"TBD" : ^15} {"TBD" : ^15} {"TBD" : ^15}' )

    return test_result;

def runBubbleTest(listToSort):
    start = perf_counter()
    test_result = bubble_sort(listToSort)
    stop = perf_counter()
    # print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {listToSort[0] : ^15} {listToSort[-1] : ^15} {listToSort[-1] - listToSort[0] : ^15}' )
    print(f'{len(listToSort) : ^15} {"": ^2} {stop - start:.5f} {"": ^4} {"TBD" : ^15} {"TBD" : ^15} {"TBD" : ^15}' )

    return test_result;


# Test Radix sort BEST case (already sorted): Ω(n+k)
printSortHeader("BEST", "RADIX")
printHeader()
runRadixTest(tst_lst.List_100_Ascending)
runRadixTest(tst_lst.List_1K_Ascending)
runRadixTest(tst_lst.List_10K_Ascending)

# Test Radix sort AVERAGE (random) case: θ(nk)
printSortHeader("AVERAGE", "RADIX")
printHeader()
runRadixTest(tst_lst.List_100_Random)
runRadixTest(tst_lst.List_1K_Random)
runRadixTest(tst_lst.List_10K_Random)

# Test Radix sort WORST case O(nk):
printSortHeader("WORST", "RADIX")
printHeader()
runRadixTest(tst_lst.List_100_Reversed)
runRadixTest(tst_lst.List_1K_Reversed)
runRadixTest(tst_lst.List_10K_Reversed)

#Starting the Bubble Sort Test
print("-----------------------------------------------------------------------------")
# Test Bubble sort BEST case (already sorted): Ω(n)
printSortHeader("BEST", "BUBBLE")
printHeader()
runBubbleTest(tst_lst.List_100_Ascending)
runBubbleTest(tst_lst.List_1K_Ascending)
runBubbleTest(tst_lst.List_10K_Ascending)

# Test Bubble sort AVERAGE (random) case: θ(n^2)
printSortHeader("AVERAGE", "BUBBLE")
printHeader()
runBubbleTest(tst_lst.List_100_Random)
runBubbleTest(tst_lst.List_1K_Random)
runBubbleTest(tst_lst.List_10K_Random)

# Test Bubble sort WORST case O(n^2):
printSortHeader("WORST", "BUBBLE")
printHeader()
runBubbleTest(tst_lst.List_100_Reversed)
runBubbleTest(tst_lst.List_1K_Reversed)
runBubbleTest(tst_lst.List_10K_Reversed)

#Starting the Merge Sort Test
print("-----------------------------------------------------------------------------")
# Test Merge sort BEST case (already sorted): Ω(n log(n))
printSortHeader("BEST", "MERGE")
printHeader()
runMergeTest(tst_lst.List_100_Ascending)
runMergeTest(tst_lst.List_1K_Ascending)
runMergeTest(tst_lst.List_10K_Ascending)

# Test Merge sort AVERAGE (random) case: θ(n log(n))
printSortHeader("AVERAGE", "MERGE")
printHeader()
runMergeTest(tst_lst.List_100_Random)
runMergeTest(tst_lst.List_1K_Random)
runMergeTest(tst_lst.List_10K_Random)

# Test Merge sort WORST case O(n log(n)):
printSortHeader("WORST", "MERGE")
printHeader()
runMergeTest(tst_lst.List_100_Reversed)
runMergeTest(tst_lst.List_1K_Reversed)
runMergeTest(tst_lst.List_10K_Reversed)
