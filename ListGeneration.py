# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 22:01:34 2022

@author: Trent
"""

import random

# Generates new list of integers each time this object is created.
# Used for testing various sorting algorithms in Main.py.
class ListGeneration:
    def __init__(self):
        # Since all same, can copy values from prev list rather than re-gen.
        self.List_100_Ascending = [x for x in range(100)]
        self.List_1K_Ascending = list.copy(self.List_100_Ascending)
        self.List_1K_Ascending += [x for x in range(100, 1_000)]
        self.List_10K_Ascending = list.copy(self.List_1K_Ascending)
        self.List_10K_Ascending += [x for x in range(1_000, 10_000)]
        
        # Larger variance = longer sort time, don't want too big b/c bbl is quad
        self.List_100_Random = [random.randint(0, 100_000) for x in range(100)]
        self.List_1K_Random = [random.randint(0, 100_000) for x in range(1_000)]
        self.List_10K_Random = [random.randint(0, 100_000) for x in range(10_000)]
        
        self.List_100_Reversed = [x for x in reversed(range(100))]
        self.List_1K_Reversed = [x for x in reversed(range(0, 1_000))]
        self.List_10K_Reversed = [x for x in reversed(range(0, 10_000))]
