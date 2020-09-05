# -*- coding: utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s == pattern:
            return True
        if len(pattern) > 1 and pattern[1] == '*':
            if s and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        elif s and pattern and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False