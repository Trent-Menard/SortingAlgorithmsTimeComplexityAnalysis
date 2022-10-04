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
#import random(Dont need since in ListGeneration)

# READ: Quicksort isn't working rn. Either fix bug or find new alg.
# Code is messy & repetitive but I plan on making functions to clean it up later

# Use the same data set for each algorithm.
tst_lst = ListGeneration()

def runRadixTest(listToSort):
    start = perf_counter()
    test_result = radixSort(listToSort)
    stop = perf_counter()
    print("\t" + str(len(listToSort)) + "\t\t\t\t" + str(stop - start))
    return test_result;

# Test Radix sort BEST case (already sorted): Ω(n+k)
print("Running BEST Case for RADIX Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runRadixTest(tst_lst.List_100_Ascending)
runRadixTest(tst_lst.List_1K_Ascending)
runRadixTest(tst_lst.List_10K_Ascending)

# Test Radix sort AVERAGE (random) case: θ(nk)
print("\nRunning AVERAGE Case for RADIX Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runRadixTest(tst_lst.List_100_Random)
runRadixTest(tst_lst.List_1K_Random)
runRadixTest(tst_lst.List_10K_Random)

# Test Radix sort WORST case O(nk):
print("\nRunning WORST Case for RADIX Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runRadixTest(tst_lst.List_100_Random)
runRadixTest(tst_lst.List_1K_Random)
runRadixTest(tst_lst.List_10K_Random)

#Starting the Bubble Sort Test
def runBubbleTest(listToSort):
    start = perf_counter()
    test_result = bubble_sort(listToSort)
    stop = perf_counter()
    print("\t" + str(len(listToSort)) + "\t\t\t\t" + str(stop - start))
    return test_result;

# Test Bubble sort BEST case (already sorted): Ω(n)
print("Running BEST Case for BUBBLE Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runBubbleTest(tst_lst.List_100_Ascending)
runBubbleTest(tst_lst.List_1K_Ascending)
runBubbleTest(tst_lst.List_10K_Ascending)

# Test Bubble sort AVERAGE (random) case: θ(n^2)
print("\nRunning AVERAGE Case for BUBBLE Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runBubbleTest(tst_lst.List_100_Random)
runBubbleTest(tst_lst.List_1K_Random)
runBubbleTest(tst_lst.List_10K_Random)

# Test Bubble sort WORST case O(n^2):
print("\nRunning WORST Case for BUBBLE Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runBubbleTest(tst_lst.List_100_Random)
runBubbleTest(tst_lst.List_1K_Random)
runBubbleTest(tst_lst.List_10K_Random)

#Starting the Merge Sort Test
def runMergeTest(listToSort):
    start = perf_counter()
    test_result = merge_sort(listToSort)
    stop = perf_counter()
    print("\t" + str(len(listToSort)) + "\t\t\t\t" + str(stop - start))
    return test_result;

# Test Merge sort BEST case (already sorted): Ω(n log(n))
print("Running BEST Case for MERGE Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runMergeTest(tst_lst.List_100_Ascending)
runMergeTest(tst_lst.List_1K_Ascending)
runMergeTest(tst_lst.List_10K_Ascending)

# Test Merge sort AVERAGE (random) case: θ(n log(n))
print("\nRunning AVERAGE Case for MERGE Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runMergeTest(tst_lst.List_100_Random)
runMergeTest(tst_lst.List_1K_Random)
runMergeTest(tst_lst.List_10K_Random)

# Test Merge sort WORST case O(n log(n)):
print("\nRunning WORST Case for MERGE Sort:")
print("\tSize:\t\t\t\tTime Elapsed:")
runMergeTest(tst_lst.List_100_Random)
runMergeTest(tst_lst.List_1K_Random)
runMergeTest(tst_lst.List_10K_Random)
