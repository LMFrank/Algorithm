#!/usr/bin/env python
# -*- coding: utf-8 -*-

def select_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array

if __name__ == '__main__':
    arrayA = [4, 9, 5, 7, 2, 1, 8, 6, 3]
    print(arrayA)
    print(select_sort(arrayA))