# -*- coding: utf-8 -*-
def quick_sort(array):
    if not array:
        return []
    pivot = array[0]
    left = quick_sort([x for x in array[1:] if x < pivot])
    right = quick_sort([x for x in array[1:] if x >= pivot])
    return left + [pivot] + right

if __name__ == '__main__':
    alist = [4, 9, 0, 7, 2, 1, 3, 6, 8]
    res = quick_sort(alist)
    print(res)