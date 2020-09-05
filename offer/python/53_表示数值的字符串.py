# -*- coding: utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        hasE = False
        hasDot = False
        hasSign = False

        for i in range(len(s)):
            if s[i] == 'e' or s[i] == 'E':
                if hasE or i == len(s) - 1:
                    return False
                hasE = True
            elif s[i] == '.':
                if hasDot or hasE:
                    return False
                hasDot = True
            elif s[i] == '+' or s[i] == '-':
                if hasSign and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
                if not hasSign:
                    if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                        return False
                hasSign = True
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
            return True