# -*- coding: utf-8 -*-
def merge_sort(array):
    n = len(array)
    if n < 2:
        return array
    mid = n // 2
    left = merge_sort(array[0:mid])
    right = merge_sort(array[mid:n])
    return merge(right, left)

def merge(left, right):
    p1 = p2 = 0
    result = []
    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            result.append(left[p1])
            p1 += 1
        else:
            result.append(right[p2])
            p2 += 1
    result += left[p1:]
    result += right[p2:]
    return result


if __name__ == '__main__':
    arrayA = [4, 9, 0, 7, 2, 1, 3, 6, 8]
    print(arrayA)
    print(merge_sort(arrayA))
