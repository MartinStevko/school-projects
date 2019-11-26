from random import sample
import functools
import time
import matplotlib.pyplot as plt
import pandas as pd


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        global bubble_times, quick_times, heap_times
        if func.__name__ == 'bubble_sort':
            bubble_times.append(run_time)
        elif func.__name__ == 'quick_sort':
            quick_times.append(run_time)
        elif func.__name__ == 'heap_sort':
            heap_times.append(run_time)

        return value
    return wrapper_timer


@timer
def bubble_sort(a):
    ch = len(a)-1
    while ch > 0:
        stop = ch
        ch = 0
        for i in range(stop):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                ch = i

    return a


def r_quick_sort(a):
    l = len(a)
    if l <= 1:
        return a

    left = []
    right = []
    p = a[l//2]
    for i in range(l):
        if a[i] < p:
            left.append(a[i])
        else:
            right.append(a[i])

    return r_quick_sort(left) + r_quick_sort(right)


@timer
def quick_sort(a):
    return r_quick_sort(a)


def build_heap(a, i):
    while 2*i < len(a)-1:
        if a[2*i] > a[2*i+1]:
            n = 2*i
        else:
            n = 2*i+1

        if a[i] < a[n]:
            a[i], a[n] = a[n], a[i]
            i = n
        else:
            break

    if 2*i == len(a)-1 and a[i] < a[2*i]:
        a[i], a[2*i] = a[2*i], a[i]

    return a


@timer
def heap_sort(a):
    a = [None] + a
    l = len(a)
    b = l//2

    while b > 0:
        build_heap(a, b)
        b -= 1

    i = 1
    while 1 < l-i:
        a[1], a[-i] = a[-i], a[1]
        a = build_heap(a[:-i], 1)+a[l-i:]
        i += 1

    return a[1:]



    return sorted(a)


sizes = [128, 256, 512, 1024, 2048, 4096]
bubble_times = []
quick_times = []
heap_times = []
for size in sizes:
    arr = sample(range(10000000), k=size)
    s = sorted(arr)

    b = bubble_sort(arr)
    assert b == s, 'Bubble: '+str(b)
    q = quick_sort(arr)
    assert q == s, 'Quick: '+str(q)
    h = heap_sort(arr)
    assert h == s, 'Heap: '+str(h)

b_data = pd.DataFrame({
    'x': range(7, 13),
    'y': bubble_times,
})
q_data = pd.DataFrame({
    'x': range(7, 13),
    'y': quick_times,
})
h_data = pd.DataFrame({
    'x': range(7, 13),
    'y': heap_times,
})

plt.plot('x', 'y', data=b_data, label='Bubble sort', linestyle='-', marker='o')
plt.plot('x', 'y', data=q_data, label='Quick sort', linestyle='-', marker='o')
plt.plot('x', 'y', data=h_data, label='Heap sort', linestyle='-', marker='o')
plt.legend(loc='upper left')
plt.show()
