#!/usr/bin/env python


def mergeSort(alist):
    if len(alist) > 1:
        middle = len(alist)//2
        left = alist[:middle]
        right = alist[middle:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                alist[k] = right[j]
                j = j + 1
            else:
                alist[k] = left[i]
                i = i + 1
            k = k + 1

        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1


if __name__ == "__main__":
    alist = [1, 7, 2, 4, 3, 5, 6]
    mergeSort(alist)
    print(alist)
