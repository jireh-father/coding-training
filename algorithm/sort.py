import random


def merge_sort(l):
    if len(l) <= 1:
        return l

    mid_idx = int(len(l) / 2)
    left = l[:mid_idx]
    right = l[mid_idx:]

    left = merge_sort(left)
    right = merge_sort(right)

    i = 0
    j = 0
    result = []
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


def bubble_sort(l):
    for last_idx in range(len(l) - 1, 0, -1):
        for i in range(last_idx):
            if l[i] > l[i + 1]:
                tmp = l[i]
                l[i] = l[i + 1]
                l[i + 1] = tmp
    return l


def selection_sort(l):
    for start_idx in range(0, len(l)):
        min_idx = start_idx
        for i in range(start_idx + 1, len(l)):
            if l[i] < l[min_idx]:
                min_idx = i
        if min_idx != start_idx:
            tmp = l[min_idx]
            l[min_idx] = l[start_idx]
            l[start_idx] = tmp
    return l


def insertion_sort(l):
    for target_idx in range(1, len(l)):
        cur_val = l[target_idx]
        cur_idx = target_idx
        while cur_idx > 0 and l[cur_idx - 1] > cur_val:
            l[cur_idx] = l[cur_idx - 1]
            cur_idx -= 1
        l[cur_idx] = cur_val
    return l


def merge_sort2(l):
    if len(l) <= 1:
        return l

    mid = int(len(l) / 2)
    left = merge_sort2(l[:mid])
    right = merge_sort2(l[mid:])

    i = 0
    j = 0
    result = []
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


import time

rlist = random.sample(range(1, 1001), 1000)

print(rlist)
start = time.time()
print(merge_sort(rlist))
print("merge_sort", time.time() - start)

print(rlist)
start = time.time()
print(bubble_sort(rlist.copy()))
print("bubble_sort", time.time() - start)

print(rlist)
start = time.time()
print(selection_sort(rlist.copy()))
print("selection_sort", time.time() - start)

print(rlist)
start = time.time()
print(insertion_sort(rlist.copy()))
print("insertionSort", time.time() - start)

print(rlist)
start = time.time()
print(merge_sort2(rlist))
print("merge2", time.time() - start)
# todo: bubble, selection, merge, quick sort, timsort, radix sort, bucket sort
