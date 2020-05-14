# -*- coding: utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        res = [0, 1, 2]
        for i in range(3, number + 1):
            res.append(res[i-1] + res[i-2])
        return res[number]