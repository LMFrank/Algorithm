# -*- coding: utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        list1 = []
        list2 = []
        n = len(array)
        for i in range(n):
            if array[i] % 2 == 0:
                list2.append(array[i])
            elif array[i] % 2 == 1:
                list1.append(array[i])
        list1.extend(list2)
        return list1