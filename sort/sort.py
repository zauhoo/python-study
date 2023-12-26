#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 0:40
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : sort.py

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insert_sort(arr):
    for i in range(1, len(arr)):
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > arr[i]:
            arr[pre_index + 1] = arr[pre_index]
            pre_index = pre_index - 1
        arr[pre_index + 1] = arr[i]
    return arr


def shell_sort(arr):
    pass


def merge_sort(arr):
    pass


def quick_sort(arr):
    pass


def counting_sort(arr):
    pass


def bucket_sort(arr):
    pass


def radix_sort(arr):
    pass


if __name__ == '__main':
    my_list = [1, 3, 2, 5, 4]
    bubble_sort(my_list)
    print(my_list)
