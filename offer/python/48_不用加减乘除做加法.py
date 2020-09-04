# -*- coding: utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            result = (num1 ^ num2) & 0xFFFFFFFF
            carry = ((num1 & num2) << 1) & 0xFFFFFFFF
            num1 = result
            num2 = carry
        if num1 <= 0x7FFFFFFF:
            result = num1
        else:
            result = ~(num1 ^ 0xFFFFFFFF)
        return result