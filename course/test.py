def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j] < alist[j-gap]:
                alist[j], alist[j-gap] = alist[j-gap], alist[j]
                j -= gap
        gap = gap // 2
    return alist


if __name__ == '__main__':
    arrayA = [4, 9, 0, 7, 3, 6, 2, 1, 8]
    print(arrayA)
    print(shell_sort(arrayA))