# -*- coding: utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s is None or len(s) == 0:
            return s
        stack = []
        for i in s.split(' '):
            stack.append(i)
        res = ''
        while len(stack) > 0:
            res += stack.pop() + ' '
        return res[:-1]
