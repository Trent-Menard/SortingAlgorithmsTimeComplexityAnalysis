# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:59:27 2022

@author: Trent
"""

from RadixSort import RadixSort as radix
from MergeSort import MergeSort as merge
from BubbleSort import BubbleSort as bubble

from ListGeneration import ListGeneration

# READ: Quicksort isn't working rn. Either fix bug or find new alg.
# Code is messy & repetitive but I plan on making functions to clean it up later

# Use the same data set for each algorithm.
tst_lst = ListGeneration(0)

res = radix()
mer = merge()
bbl = bubble()

def printHeader():
    print(f'{"Size" : ^15} {"Time Elapsed" : ^15} {"Min" : ^15} {"Max" : ^10} {"Range" : ^15}')
    
def printSortHeader(sort, sortCase):
    print()
    print(f'{"" : ^24} Running {sort} Case for {sortCase} Sort')

# Run each dataset for each sorting algorithm

# These tests could be combined in for loop but is 
# designed this way for propor formatting

# Test Radix sort BEST case (already sorted): Ω(n+k)
printSortHeader("BEST", "RADIX")
printHeader()
for x in tst_lst.cumulative_dataset_ascending:
    res.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {res.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')

# Test Radix sort AVERAGE (random) case: θ(nk)
printSortHeader("AVERAGE", "RADIX")
printHeader()
for x in tst_lst.cumulative_dataset_random:
    res.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {res.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')
    
# Test Radix sort WORST case O(nk):
printSortHeader("WORST", "RADIX")
printHeader()
for x in tst_lst.cumulative_dataset_descending:
    res.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {res.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')
    
print("----------------------------------------------------------------------")
#Starting the Merge Sort Test

# Test Merge sort BEST case (already sorted): Ω(n log(n))
printSortHeader("BEST", "MERGE")
printHeader()
for x in tst_lst.cumulative_dataset_ascending:
    mer.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {mer.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')

# Test Merge sort AVERAGE (random) case: θ(n log(n))
printSortHeader("AVERAGE", "MERGE")
printHeader()
for x in tst_lst.cumulative_dataset_random:
    mer.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {mer.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')

# Test Merge sort WORST case O(n log(n)):
printSortHeader("WORST", "MERGE")
printHeader()
for x in tst_lst.cumulative_dataset_descending:
    mer.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {mer.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')

# print("----------------------------------------------------------------------")
#Starting the Bubble Sort Test

printSortHeader("BEST", "BUBBLE")
printHeader()
for x in tst_lst.cumulative_dataset_ascending:
    bbl.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {bbl.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')

printSortHeader("AVERAGE", "BUBBLE")
printHeader()
for x in tst_lst.cumulative_dataset_random:
    bbl.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {bbl.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')

printSortHeader("WORST", "BUBBLE")
printHeader()
for x in tst_lst.cumulative_dataset_descending:
    bbl.sort(x)
    print(f'{len(x) : ^15} {"": ^2} {bbl.timing:.5f} {"": ^4} {min(x) : ^15} {max(x) : ^10} {max(x) - min(x) : ^15}')
print("----------------------------------------------------------------------")
#Starting the QuickSort Test

# Test QuickSorts Best and Average case: θ(n log(n)) 
# (Randomized numbers, AKA: NOT SORTED)
#printSortHeader("AVERAGE", "QUICK")
#runQuickSort(tst_lst.List_100_Random)
#runQuickSort(tst_lst.List_1K_Random)
#runQuickSort(tst_lst.List_10K_Random)
#runQuickSort(tst_lst.List_10K_Random)
#runQuickSort(tst_lst.List_100QuiK_Random)

# printSortHeader("WORST", "QUICK")
#runQuickSort(tst_lst.List_100_Ascending)
#runQuickSort(tst_lst.List_1K_Ascending)
#runQuickSort(tst_lst.List_10K_Ascending)
#runQuickSort(tst_lst.List_100K_Ascending)
