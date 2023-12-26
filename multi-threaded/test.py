#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 0:13
# @Author  : Xuhaozhang
# @Email   : xuhaozhang_hfut@163.com
# @File    : mysql_conn.py

import threading
from contextlib import contextmanager

# 用来存储local的数据
_local = threading.local()


@contextmanager
def acquire(*locks):
    # 对锁按照id进行排序
    locks = sorted(locks, key=lambda x: id(x))

    # 如果已经持有锁当中的序号有比当前更大的，说明策略失败
    acquired = getattr(_local, 'acquired', [])

    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # 获取所有锁
    acquired.extend(locks)
    _local.acquired = acquired
    print(_local.acquired)

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # 倒叙释放
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


def philosopher(left, right):
    for i in range(5):
        with acquire(left, right):
            print(threading.currentThread(), 'eating', i)


# 叉子的数量
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

for chopstick in chopsticks:
    print(id(chopstick))

for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n], chopsticks[(n + 1) % NSTICKS]))
    t.start()
