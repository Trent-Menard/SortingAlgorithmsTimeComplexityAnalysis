# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 22:01:34 2022

@author: Trent
"""
import numpy as np
# ascending_ints_100

# Generates new list of integers each time this object is created.
# Used for testing various sorting algorithms in Main.py.
class ListGeneration:
    def __init__(self, useSeed=None):
        # Generator w/ random seed
        rng = np.random.default_rng()
        
        # Generator w/ provided seed
        if useSeed is not None:
            rng = np.random.default_rng(seed=useSeed)
        # Create & fill array w/ ascending values in range using numpy
        # Numpy returns ndarray object so convert to Python list so sorts can modify
        self.List_100_Ascending = np.arange(100).tolist()
        self.List_1K_Ascending = np.arange(1_000).tolist()
        self.List_10K_Ascending = np.arange(10_000).tolist()
        
        # Create & fill array w/ descending values in range
        self.List_100_Reversed = np.arange(start=100, stop=0, step=-1).tolist()
        self.List_1K_Reversed = np.arange(start=1_000, stop=0, step=-1).tolist()
        self.List_10K_Reversed = np.arange(start=10_000, stop=0, step=-1).tolist()
        
        # Larger variance = longer sort time, don't want too big b/c bbl is quad
        # Create & fill array w/ random values in range
        self.List_100_Random = rng.integers(low=0, high=100_000, size=100).tolist()
        self.List_1K_Random = rng.integers(low=0, high=100_000, size=1_000).tolist()
        self.List_10K_Random = rng.integers(low=0, high=100_000, size=10_000).tolist()
        
        # These are lists of the respective datasets
        self.cumulative_dataset_ascending = [self.List_100_Ascending, self.List_1K_Ascending, self.List_10K_Ascending]
        self.cumulative_dataset_descending = [self.List_100_Reversed, self.List_1K_Reversed, self.List_10K_Reversed]
        self.cumulative_dataset_random = [self.List_100_Random, self.List_1K_Random, self.List_10K_Random]
