# -*- coding: utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data is None:
            return 0
        if self.GetLastK(data, k) == -1 or self.GetFirstK(data, k) == -1:
            return 0
        return self.GetLastK(data, k) - self.GetFirstK(data, k) + 1

    def GetFirstK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] == k and (mid == low or data[mid - 1] != k):
                return mid
            else:
                high = mid - 1
        return -1

    def GetLastK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > k:
                high = mid - 1
            elif data[mid] == k and (mid == high or data[mid + 1] != k):
                return mid
            else:
                low = mid + 1
        return -1