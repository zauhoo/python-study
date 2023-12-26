#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 0:22
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : search_judge.py

import json
import time
import random
import psutil
import functools

json_filename = 'data.json'
a = {'cpu': 14, 'mem': 70}
data_list = list()


def generator_json():
    # 生成包含字典的列表
    global data_list
    # 列表的长度
    list_length = 10000

    for _ in range(list_length):
        # 随机生成cpu和mem的值
        cpu_value = random.randint(10, 20)
        mem_value = random.randint(50, 100)

        # 创建字典并添加到列表中
        data_dict = {'cpu': cpu_value, 'mem': mem_value}
        data_list.append(data_dict)

    # 将列表写入JSON文件
    with open(json_filename, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"数据已写入到 {json_filename}")


def read_json():
    global data_list
    # 读取JSON文件
    with open(json_filename, 'r') as json_file:
        data_list = json.load(json_file)

def dict_sort():
    global data_list
    # 定义一个函数来提取CPU值
    def get_cpu(item):
        return item['cpu']

    # 使用sorted()函数对列表b进行排序，按CPU值排序
    data_list.sort(key=get_cpu)


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} 执行时间：{execution_time:.10f} 秒")
        return result
    return wrapper


def memory_usage_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 获取当前进程的内存使用情况
        process = psutil.Process()
        start_memory = process.memory_info().rss

        # 调用原始函数
        result = func(*args, **kwargs)

        # 获取调用后的内存使用情况
        end_memory = process.memory_info().rss
        memory_used = end_memory - start_memory

        print(
            f"{func.__name__} 内存使用情况：{memory_used / (1024 ** 2):.10f} MB")

        return result

    return wrapper


@timing_decorator
@memory_usage_decorator
def generator_filter():
    global data_list
    print("generator_filter")
    if any(item['cpu'] > a['cpu'] and item['mem'] > a['mem'] for item in
           data_list):
        print("b中至少存在一项满足条件。")
    else:
        print("b中没有元素满足条件。")


@timing_decorator
@memory_usage_decorator
def dichotomy_filter():
    global data_list
    print("dichotomy_filter")
    left, right = 0, len(data_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if data_list[mid]['cpu'] > a['cpu'] and data_list[mid]['mem'] > a['mem']:
            print("b中至少存在一项满足条件。")
            return
        elif data_list[mid]['cpu'] < a['cpu'] or data_list[mid]['mem'] < a['mem']:
            left = mid + 1
        else:
            right = mid - 1
    print("b中没有元素满足条件。")


if __name__ == '__main__':
    read_json()
    generator_filter()
    dict_sort()
    dichotomy_filter()
