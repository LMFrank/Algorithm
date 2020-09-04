# -*- coding: utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        self.getSum(n)
        return self.sum

    def getSum(self, n):
        self.sum += n
        n -= 1
        return n > 0 and self.getSum(n)