# -*- coding: utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def quick_sort(array):
            if not array:
                return []
            pivot = array[0]
            left = quick_sort([x for x in array[1:] if x < pivot])
            right = quick_sort([x for x in array[1:] if x > pivot])
            return left + [pivot] + right

        if tinput == [] or k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[:k]