# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:29:49 2022

@author: Ryan

Code adopted from: https://www.geeksforgeeks.org/python-program-for-quicksort/
"""

# Python program for implementation of Quicksort Sort
# This method utilizes making the middle element of an unsorted array the pivot

# Function to find the partition position
def partition(array, low, high):
 
    # choose the center element as pivot
    pivot = array[len(round(array)/2)]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort Best case
def quickBest(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickBest(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickBest(array, pi + 1, high)
        
        

# Functions to perform quicksort Worst case
# Worst case happens when the pivot is an extreme (smallest size element or largest)
# to force this we sort the array and then apply the highest element in the array

# Function to find the partition position
def partition2(array, low, high):
 
    # choose the right most element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 

def quickWorst(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition2(array, low, high)
 
        # Recursive call on the left of pivot
        quickWorst(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickWorst(array, pi + 1, high)