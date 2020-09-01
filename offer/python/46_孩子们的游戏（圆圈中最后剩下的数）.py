# -*- coding: utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n and not m:
            return -1
        res = range(n)
        i = 0
        while len(res) > 1:
            i = (m + i - 1) % len(res)
            res.pop(i)
        return res[0]