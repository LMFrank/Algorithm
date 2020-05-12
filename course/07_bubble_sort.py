#!/usr/bin/env python
# -*- coding: utf-8 -*-

def bubble_sort(array):
    """冒泡排序"""
    n = len(array)
    for j in range(n - 1):
        count = 0
        for i in range(n - 1 - j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                count += 1
        if 0 == count:
            break
    return array

if __name__ == '__main__':
    arrayA = [4, 2, 6, 1, 5]
    print(arrayA)
    print(bubble_sort(arrayA))