# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:59:27 2022

@author: Trent
"""

from BubbleSort import bubble_sort
# from QuickSort import quick_sort
from MergeSort import merge_sort
from RadixSort import radixSort

import random
from time import perf_counter

# READ: Quicksort isn't working rn. Either fix bug or find new alg.
# Code is messy & repetitive but I plan on making functions to clean it up later

Test_100_Result = []
Test_1K_Result = []
Test_10K_Result = []

# Ascending lists (for already sorted data test)
Test_100 = [x for x in range(100)]

Test_1K = list.copy(Test_100)
Test_1K += [x for x in range(100, 1_000)]

Test_10K = list.copy(Test_1K)
Test_10K += [x for x in range(1_000, 10_000)]

# Test Radix sort BEST case: Ω(n+k)
print("Running BEST Case for RADIX Sort:")
start = perf_counter()
Test_100_Result = radixSort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))

start = perf_counter()
radixSort(Test_1K)
stop = perf_counter()
print("  1,000\t\t\t\t" + str(stop - start))

start = perf_counter()
radixSort(Test_10K)
stop = perf_counter()
print("  10,000\t\t\t" + str(stop - start))


# Random numbers list (for unsorted data test)
print("\n*Generating random data, one moment please...*\n")
Test_100 = [random.randint(0, 100) for x in range(100)]

Test_1K = [random.randint(0, 1_000) for x in range(0, 1_000)]

Test_10K = [random.randint(0, 10_000) for x in range(0, 10_000)]

print(Test_100)

# Test Radix sort AVERAGE case: θ(nk)
print("Running AVERAGE Case for RADIX Sort:")
start = perf_counter()
Test_100_Result = radixSort(Test_100)
stop = perf_counter()
print("  Size:\t\t\t\tTime Elapsed:")
print("  100\t\t\t\t" + str(stop - start))
start = perf_counter()
Test_1K_Result = radixSort(Test_1K)
stop = perf_counter()
print("  1,000\t\t\t\t" + str(stop - start))

start = perf_counter()
Test_10K_Result = radixSort(Test_10K)
stop = perf_counter()
print("  10,000\t\t\t" + str(stop - start))
