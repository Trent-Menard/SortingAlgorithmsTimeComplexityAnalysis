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

rdx = radix()
mer = merge()
bbl = bubble()
quk = quick()

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
        rdx.sort(x)
        print(f'  Radix: {rdx.timing:.5f} s')
        # Test Merge sort BEST case (already sorted): Ω(n log(n))
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
    else:
        rdx.sort(x)
        print(f'  Radix: {rdx.timing:.5f} s')
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
        bbl.sort(x)
        print(f'  Bubble: {bbl.timing:.5f} s')
        quk.sort(x, min(x), min(x), 0)
        print(f'  Quick: {quk.timing:.5f} s')
        print()

printLineSeparation()
    
printSortHeader("AVERAGE", "RADIX / MERGE / BUBBLE")
for x in tst_lst.cumulative_dataset_random:
    print("Size: " + str(len(x)))
    if len(x) == 100_000:
        # Test Radix sort AVERAGE (random) case: θ(nk)
        rdx.sort(x)
        print(f'  Radix: {rdx.timing:.5f} s')
        # Test Merge sort AVERAGE (random) case: θ(n log(n))
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
    else:
        rdx.sort(x)
        print(f'  Radix: {rdx.timing:.5f} s')
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
        rdx.sort(x)
        print(f'  Radix: {rdx.timing:.5f} s')
        # Test Merge sort WORST case O(n log(n)):
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
        print("  Bubble: Too computationally expensive")
    else:
        rdx.sort(x)
        print(f'  Radix: {rdx.timing:.5f} s')
        mer.sort(x)
        print(f'  Merge: {mer.timing:.5f} s')
        bbl.sort(x)
        print(f'  Bubble: {bbl.timing:.5f} s')
    print()
    
printLineSeparation()

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

    
radix_results = "RADIX Results:\n"
for x in rdx.timing_results:
    for x, y in zip(x.keys(), x.values()):
        radix_results += x + "\t\t\t" + str(y) + "\n"
        
print(radix_results)
        
# print("\nMERGE Results:\n")
# for x in mer.timing_results:
#     for y in x.keys():
#         for z in x.values():
#             print(y + "\t\t\t" + str(z) + " seconds")

# print("\BUBBLE Results:\n")
# for x in bbl.timing_results:
#     for y in x.keys():
#         for z in x.values():
#             print(y + "\t\t\t" + str(z) + " seconds")
            
#Starting the QuickSort Test
# Test QuickSorts Best and Average case: θ(n log(n))
