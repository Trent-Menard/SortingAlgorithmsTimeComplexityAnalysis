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

def printSortHeader(sort, sortCase):
    print()
    print(f'{"" : ^8} Running {sort} Case for {sortCase} Sort')
    
def printLineSeparation():
    for x in range(1, 69):
        print("-", end="")
    print()

all_timing_merge = []
all_timing_radix = []
all_timing_bubble = []
all_timing_quick= []

quk = quick()
quk.sort(tst_lst.List_100K_Random)
print(f'Quick sort sorted {len(quk.sorted)} elements in {quk.timing} seconds')

# New <sorting algorithm> object is created each time a dataset is run and we are 
# appending the results of each timing to a cumulative list.

def enum(listToEnum):
    for x in enumerate(listToEnum):
        
        if x[0] == 0:
            printSortHeader("BEST", "RADIX / MERGE / BUBBLE")
        elif x[0] == 1:
            printSortHeader("AVERAGE", "RADIX / MERGE / BUBBLE")
        elif x[0] == 2:
            printSortHeader("WORST", "RADIX / MERGE / BUBBLE")
        # Size 100,000 is computationally too expensive for Bubble & Quick sort so skip.
        if len(x[1]) == 100_000:
            mergeSrt = merge()
            mergeSrt.sort(x[1])
            all_timing_merge.append(mergeSrt.timing_results)
            print(f'Size: {len(x[1])}')
            print(f'  Merge: {mergeSrt.timing:.5f} s')
    
            radixSrt = radix()
            radixSrt.sort(x[1])
            all_timing_radix.append(radixSrt.timing_results)
            print(f'  Radix: {radixSrt.timing:.5f} s')
            
            print("  Bubble: Computationally too expensive")
            # print(f'  Quick: {radixSrt.timing:.5f} s')
    
        else:
            mergeSrt = merge()
            mergeSrt.sort(x[1])
            all_timing_merge.append(mergeSrt.timing_results)
            print(f'Size: {len(x[1])}')
            print(f'  Merge: {mergeSrt.timing:.5f} s')
    
            radixSrt = radix()
            radixSrt.sort(x[1])
            all_timing_radix.append(radixSrt.timing_results)
            print(f'  Radix: {radixSrt.timing:.5f} s')
    
            bubbleSrt = bubble()
            bubbleSrt.sort(x[1])
            all_timing_bubble.append(bubbleSrt.timing_results)
            print(f'  Bubble: {bubbleSrt.timing:.5f} s')
            
        print()
            
enum(tst_lst.cumulative_dataset_ascending)
enum(tst_lst.cumulative_dataset_random)
    
# print("rdx best")
# for a in rdx_best.timing_results:
#     for x, y in zip(a.keys(), a.values()):
#         print(x + " -> " + str(y))

# print("RADIX sort BEST case:")
# for x in all_timing_radix:
#     print(x)

        # Test Radix sort BEST case (already sorted): Ω(n+k)
        # Test Merge sort BEST case (already sorted): Ω(n log(n))

        # Test Radix sort AVERAGE (random) case: θ(nk)
        # Test Merge sort AVERAGE (random) case: θ(n log(n))


        # Test Radix sort WORST case O(nk):
        # Test Merge sort WORST case O(n log(n)):

# printSortHeader("BEST", "BUBBLE")
# # Best case : pivot is middle & random data
# quk.sort(tst_lst.List_100K_Random, True)
# print("Optomized Pivot: " + str(quk.timing))

# printSortHeader("WORST", "BUBBLE")
# # Worst case : pivot is extreme (end or beginning) & pre-sorted (ascending) list
# quk.sort(tst_lst.List_10K_Ascending, False)
# print("Unoptomized Pivot: " + str(quk.timing))


# with open("Results.txt", "w") as out_file:
#     out_file.writelines()

# print("\nMERGE Results:\n")
# for x in mer.timing_results:
#     for y in x.keys():
#         for z in x.values():
#             print(y + "\t\t\t" + str(z) + " seconds")

#Starting the QuickSort Test
# Test QuickSorts Best and Average case: θ(n log(n))
