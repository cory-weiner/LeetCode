# Median of Two Sorted Arrays    
from typing import List
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return statistics.median(merge_lists(nums1,nums2))

def merge_lists(lx,ly):
    x = 0
    y = 0
    len_x = len(lx)
    len_y = len(ly)
    result = []
    while x < len_x and y < len_y:

        if lx[x] < ly[y]:
            result.append(lx[x])
            x+=1
        else:
            result.append(ly[y])
            y+=1
    return result + lx[x:] + ly[y:]

list_1 = [1,3]
list_2 = [2]

print(merge_lists(list_1,list_2))