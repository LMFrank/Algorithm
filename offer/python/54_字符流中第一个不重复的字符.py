# -*- coding: utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dict = {}

    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return '#'

    def Insert(self, char):
        # write code here
        self.s = self.s + char
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1