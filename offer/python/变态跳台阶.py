# -*- coding: utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        ans = 1
        for i in range(1, number):
            ans = 2 * ans
        return ans