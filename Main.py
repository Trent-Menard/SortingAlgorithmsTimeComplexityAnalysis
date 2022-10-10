# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:59:27 2022

@author: Trent
"""

from RadixSort import RadixSort as radix
from MergeSort import MergeSort as merge
from BubbleSort import BubbleSort as bubble
from QuickSort import QuickS as quick
from ListGeneration import ListGeneration

# Use the same data set for each algorithm.
tst_lst = ListGeneration(0)

writeToFile = [""]

def printSortHeader(sort, sortCase):
    print(f'\n{"" : ^8} Running {sort} Case for {sortCase} Sort')
    writeToFile.append(f'\n{"" : ^8} Running {sort} Case for {sortCase} Sort\n')
    
def printLineSeparation():
    for x in range(1, 69):
        print("-", end="")
        writeToFile.append("-", end="")
        writeToFile.append("\n\n")
    print()

def quickSort_special_case(listToSort, isBestCase):
    # Worst case: Pivot is extreme (end or begin) & pre-sorted list
    # Best case: randomly assorted & pivot is middle element
    for x in listToSort:
        if len(x) >= 10_000:
            print(f'Size: {len(x)}\n  Quick: Computationally too expensive')
            writeToFile.append(f'Size: {len(x)}\n  Quick: Computationally too expensive\n')
        else:
            quickSrt = quick()
            quickSrt.sort(x, isBestCase)
            all_timing_quick.append(quickSrt.timing_results)
            print(f'Size: {len(x)}  \n  Quick: {quickSrt.timing:.5f} s\n')
            writeToFile.append(f'Size: {len(x)}  \n  Quick: {quickSrt.timing:.5f} s\n')
            
all_timing_merge = []
all_timing_radix = []
all_timing_bubble = []
all_timing_quick= []

# New <sorting algorithm> object is created each time a dataset is run and we are 
# appending the results of each timing to a cumulative list.
def enum(listToEnum):
    idx = 0
    for x in listToEnum:
        
        # Size 100,000 is computationally too expensive for Bubble & Quick sort so skip.
        if len(x) >= 100_000:
            mergeSrt = merge()
            mergeSrt.sort(x)
            all_timing_merge.append(mergeSrt.timing_results)
            print(f'Size: {len(x)}\n  Merge: {mergeSrt.timing:.5f} s')
            writeToFile.append(f'Size: {len(x)}\n  Merge: {mergeSrt.timing:.5f} s\n')
                
            radixSrt = radix()
            radixSrt.sort(x)
            all_timing_radix.append(radixSrt.timing_results)
            print(f'  Radix: {radixSrt.timing:.5f} s')
            print("  Bubble: Computationally too expensive")
            writeToFile.append(f'  Radix: {radixSrt.timing:.5f} s\n')
            writeToFile.append(  "Bubble: Computationally too expensive\n")

            
        # Run each dataset on each sorting algorithm.
        else:
            mergeSrt = merge()
            mergeSrt.sort(x)
            all_timing_merge.append(mergeSrt.timing_results)
            print(f'Size: {len(x)}\n  Merge: {mergeSrt.timing:.5f} s')
            writeToFile.append(f'Size: {len(x)}\n  Merge: {mergeSrt.timing:.5f} s\n')
    
            radixSrt = radix()
            radixSrt.sort(x)
            all_timing_radix.append(radixSrt.timing_results)
            print(f'  Radix: {radixSrt.timing:.5f} s')
            writeToFile.append(f'  Radix: {radixSrt.timing:.5f} s\n')
    
            bubbleSrt = bubble()
            bubbleSrt.sort(x)
            all_timing_bubble.append(bubbleSrt.timing_results)
            print(f'  Bubble: {bubbleSrt.timing:.5f} s')
            writeToFile.append(f'  Bubble: {bubbleSrt.timing:.5f} s\n')
                        
        print()
        idx + 1
            
# Test Merge sort BEST case (already sorted): Ω(n log(n))
# Test Radix sort BEST case (already sorted): Ω(n+k)
printSortHeader("BEST", "MERGE / RADIX / BUBBLE")
enum(tst_lst.cumulative_dataset_ascending)

# Test Merge sort AVERAGE (random) case: θ(n log(n))
# Test Radix sort AVERAGE (random) case: θ(nk)
printSortHeader("AVERAGE", "MERGE / RADIX / BUBBLE")
enum(tst_lst.cumulative_dataset_random)

# Test Merge sort WORST case O(n log(n)):
# Test Radix sort WORST case O(nk):
printSortHeader("WORST", "MERGE / RADIX / BUBBLE")
enum(tst_lst.cumulative_dataset_descending)
        
# Test QuickSorts Best and Average case: θ(n log(n))
printSortHeader("BEST", "QUICK")
quickSort_special_case(tst_lst.cumulative_dataset_random, isBestCase=True)

printSortHeader("WORST", "QUICK")
quickSort_special_case(tst_lst.cumulative_dataset_ascending, isBestCase=False)
    
with open("Results.txt", "w") as out_file:
    out_file.writelines(writeToFile)
