# -*- coding: utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array or not tsum:
            return []
        left = 0
        right = len(array) - 1
        while left < right:
            added = array[left] + array[right]
            if added == tsum:
                return [array[left], array[right]]
            elif added < tsum:
                left += 1
            else:
                right -= 1
        return []