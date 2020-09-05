# -*- coding: utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            temp = A[i]
            b = 1
            for j in range(len(A)):
                A[i] = 1
                b *= A[j]
            B.append(b)
            A[i] = temp
        return B