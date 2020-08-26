# -*- coding: utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(1, n+1):
            j = i
            while j > 0:
                if j % 10 == 1:
                    count += 1
                j = j // 10
        return count