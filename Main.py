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
import random

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

#The Beginning Of the Bubble Test

Test_100 = []

Test_1K = []

Test_10K = []

# Ascending lists (for already sorted data test)
Test_100 = [x for x in range(100)]

Test_1K = list.copy(Test_100)
Test_1K += [x for x in range(100, 1_000)]

Test_10K = list.copy(Test_1K)
Test_10K += [x for x in range(1_000, 10_000)]

#Test Bubble Sort BEST Case Ω(n)
print("Running BEST Case for Bubble Sort:")
start = perf_counter()
Test_100_Result = bubble_sort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))

# start = perf_counter()
# bubble_sort(Test_1K)
# stop = perf_counter()
# print("  1,000\t\t\t\t" + str(stop - start))

# start = perf_counter()
# bubble_sort(Test_10K)
# stop = perf_counter()
# print("  10,000\t\t\t" + str(stop - start))

# Random numbers list (for unsorted data test)
print("\n*Generating random data, one moment please...*\n")
Test_100 = [random.randint(0, 100) for x in range(100)]

Test_1K = [random.randint(0, 1_000) for x in range(0, 1_000)]

Test_10K = [random.randint(0, 10_000) for x in range(0, 10_000)]

#Test Bubble Sort AVERAGE Case Ω(n^2)
print("Running AVERAGE Case for Bubble Sort:")
start = perf_counter()
Test_100_Result = bubble_sort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))
start = perf_counter()
Test_1K_Result = bubble_sort(Test_1K)
stop = perf_counter()
print("  1,000\t\t\t\t" + str(stop - start))

# start = perf_counter()
# Test_10K_Result = bubble_sort(Test_10K)
# stop = perf_counter()
# print("  10,000\t\t\t" + str(stop - start))

# Reverse numbers list (for worst case sorted data test)
print("\n*Generating random data, one moment please...*\n")
Test_100 = [random.randint(0, 100) for x in reversed(range(100))]

Test_1K = [random.randint(0, 1_000) for x in reversed(range(0, 1_000))]

Test_10K = [random.randint(0, 10_000) for x in reversed(range(0, 10_000))]

#Test Bubble Sort WORST Case Ω(n^2)
print("Running WORST Case for Bubble Sort:")
start = perf_counter()
Test_100_Result = bubble_sort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))
start = perf_counter()
Test_1K_Result = bubble_sort(Test_1K)
stop = perf_counter()
print("  1,000\t\t\t\t" + str(stop - start))

start = perf_counter()
Test_10K_Result = bubble_sort(Test_10K)
stop = perf_counter()
print("  10,000\t\t\t" + str(stop - start))

#The Beginning Of the Merge Test
Test_100_Result = []
Test_1K_Result = []
Test_10K_Result = []

# Ascending lists (for already sorted data test)
Test_100 = [x for x in range(100)]

Test_1K = list.copy(Test_100)
Test_1K += [x for x in range(100, 1_000)]

Test_10K = list.copy(Test_1K)
Test_10K += [x for x in range(1_000, 10_000)]

#Test Merge Sort BEST Case Ω(n log(n))
print("Running BEST Case for Merge Sort:")
start = perf_counter()
Test_100_Result = merge_sort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))

start = perf_counter()
merge_sort(Test_1K)
stop = perf_counter()
print("  1,000\t\t\t\t" + str(stop - start))

start = perf_counter()
merge_sort(Test_10K)
stop = perf_counter()
print("  10,000\t\t\t" + str(stop - start))

# Random numbers list (for unsorted data test)
print("\n*Generating random data, one moment please...*\n")
Test_100 = [random.randint(0, 100) for x in range(100)]

Test_1K = [random.randint(0, 1_000) for x in range(0, 1_000)]

Test_10K = [random.randint(0, 10_000) for x in range(0, 10_000)]

#Test Merge Sort AVERAGE Case Θ(n log(n))
print("Running AVERAGE Case for Merge Sort:")
start = perf_counter()
Test_100_Result = merge_sort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))
start = perf_counter()
Test_1K_Result = merge_sort(Test_1K)
stop = perf_counter()
print("  1,000\t\t\t\t" + str(stop - start))

start = perf_counter()
Test_10K_Result = merge_sort(Test_10K)
stop = perf_counter()
print("  10,000\t\t\t" + str(stop - start))

# Reverse numbers list (for worst case sorted data test)
print("\n*Generating random data, one moment please...*\n")
Test_100 = [random.randint(0, 100) for x in reversed(range(100))]

Test_1K = [random.randint(0, 1_000) for x in reversed(range(0, 1_000))]

Test_10K = [random.randint(0, 10_000) for x in reversed(range(0, 10_000))]

#Test Merge Sort WORST Case O(n log(n))
print("Running WORST Case for Merge Sort:")
start = perf_counter()
Test_100_Result = merge_sort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))
start = perf_counter()
Test_1K_Result = merge_sort(Test_1K)
stop = perf_counter()
print("  1,000\t\t\t\t" + str(stop - start))

start = perf_counter()
Test_10K_Result = merge_sort(Test_10K)
stop = perf_counter()
print("  10,000\t\t\t" + str(stop - start))
