# -*- coding: utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        i = 1
        j = 2
        while i < j:
            curSum = (i +j) * (j + 1 - i) / 2
            if curSum < tsum:
                j += 1
            elif curSum == tsum:
                res.append(range(i, j+1))
                i += 1
            else:
                i += 1
        return res