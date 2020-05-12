#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insert_sort(array):
    n = len(array)
    for j in range(1, n):
        index = j
        while index > 0:
            if array[index] < array[index-1]:
                array[index], array[index-1] = array[index-1], array[index]
                index -= 1
            else:
                break
    return array

if __name__ == '__main__':
    arrayA = [4, 9, 0, 7, 3, 6, 2, 1, 8]
    print(arrayA)
    print(insert_sort(arrayA))
