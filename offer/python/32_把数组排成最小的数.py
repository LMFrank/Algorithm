# -*- coding: utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        num = [str(x) for x in numbers]
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if num[j] + num[i] < num[i] + num[j]:
                    num[i], num[j] = num[j], num[i]
        return ''.join(num)