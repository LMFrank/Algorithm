# -*- coding: utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        s = s.strip()
        if not s:
            return 0
        num, flag = 0, 1
        if s[0] == '-':
            s = s[1:]
            flag = -1
        elif s[0] == '+':
            s = s[1:]
        for n in s:
            if '0' <= n <= '9':
                num = 10 * num + int(n)
            else:
                return 0
        return flag * num