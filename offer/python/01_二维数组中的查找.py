# -*- coding: utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == []:
            return False
        n = len(array) - 1
        m = len(array[0]) - 1
        j = 0
        while j <= m and n >= 0:
            if target < array[n][j]:
                n -= 1
            elif target > array[n][j]:
                j += 1
            else:
                return True
        return False