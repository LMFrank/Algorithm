# -*- coding: utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        data = set()
        for d in array:
            if d in data:
                data.remove(d)
            else:
                data.add(d)
        return list(data)