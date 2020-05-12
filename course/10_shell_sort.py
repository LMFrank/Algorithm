# -*- coding: utf-8 -*-
def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j], alist[j-gap] = alist[j-gap], alist[j]
                j -= gap
        gap = gap // 2
    return alist

if __name__ == '__main__':
    arrayA = [4, 9, 0, 7, 2, 1, 3, 6, 8]
    print(arrayA)
    print(shell_sort(arrayA))
