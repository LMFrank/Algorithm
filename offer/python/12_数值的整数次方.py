# -*- coding: utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        res = 1
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent < 0:
            for i in range(-exponent):
                res = res * base
            return 1 / res
        for i in range(exponent):
            res = res * base
        return res