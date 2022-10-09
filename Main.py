# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:59:27 2022

@author: Trent
"""

from RadixSort import RadixSort as radix
from MergeSort import MergeSort as merge
from BubbleSort import BubbleSort as bubble
#from QuickSort import quickSort
from ListGeneration import ListGeneration

# Use the same data set for each algorithm.
tst_lst = ListGeneration(0)
res = radix()
mer = merge()
bbl = bubble()
    
def printSortHeader(sort, sortCase):
    print()
    print(f'{"" : ^8} Running {sort} Case for {sortCase} Sort')
    
def printLineSeparation():
    for x in range(1, 69):
        print("-", end="")
    print()

# Run each dataset for each sorting algorithm
# Size 100,000 is too computationally expensive for Bubbke sort, so skip.

printSortHeader("BEST", "RADIX / MERGE / BUBBLE")
for x in tst_lst.cumulative_dataset_ascending:
    print("Size: " + str(len(x)))
    if len(x) == 100_000:
        # Test Radix sort BEST case (already sorted): Ω(n+k)
        res.sort(x)
        print(f'  Radix: {res.timing:.5f} s')
        # Test Merge sort BEST case (already sorted): Ω(n log(n))
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
    else:
        res.sort(x)
        print(f'  Radix: {res.timing:.5f} s')
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
        bbl.sort(x)
        print(f'  Bubble: {bbl.timing:.5f} s')
        print()
printLineSeparation()
    
printSortHeader("AVERAGE", "RADIX / MERGE / BUBBLE")
for x in tst_lst.cumulative_dataset_random:
    print("Size: " + str(len(x)))
    if len(x) == 100_000:
        # Test Radix sort AVERAGE (random) case: θ(nk)
        res.sort(x)
        print(f'  Radix: {res.timing:.5f} s')
        # Test Merge sort AVERAGE (random) case: θ(n log(n))
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
    else:
        res.sort(x)
        print(f'  Radix: {res.timing:.5f} s')
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
        bbl.sort(x)
        print(f'  Bubble: {bbl.timing:.5f} s')
    print()
    
printLineSeparation()
    
printSortHeader("WORST", "RADIX / MERGE / BUBBLE")
for x in tst_lst.cumulative_dataset_descending:
    print("Size: " + str(len(x)))
    if len(x) == 100_000:
        # Test Radix sort WORST case O(nk):
        res.sort(x)
        print(f'  Radix: {res.timing:.5f} s')
        # Test Merge sort WORST case O(n log(n)):
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
    else:
        res.sort(x)
        print(f'  Radix: {res.timing:.5f} s')
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
        bbl.sort(x)
        print(f'  Bubble: {bbl.timing:.5f} s')
    print()


#Starting the QuickSort Test

# Test QuickSorts Best and Average case: θ(n log(n)) 
#(Randomized numbers, AKA: NOT SORTED)

#size = len(tst_lst.cumulative_dataset_random)
#rand = tst_lst.cumulative_dataset_random
#asc = tst_lst.cumulative_dataset_ascending
#desc = tst_lst.cumulative_dataset_descending

#printSortHeader("AVERAGE and Best case", "QUICK")
#printHeader()

#quickSort(tst_lst.cumulative_dataset_random,0,size-1)

# printSortHeader("WORST", "QUICK")
#quick(tst_lst.List_100_Ascending)
#runQuickSort(tst_lst.List_1K_Ascending)
#runQuickSort(tst_lst.List_10K_Ascending)
#runQuickSort(tst_lst.List_100K_Ascending)
    
