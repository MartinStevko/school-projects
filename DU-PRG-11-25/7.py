from random import sample
import functools
import time
import matplotlib.pyplot as plt
import pandas as pd

def timer(data):
    def wrapper(func):
        def wrapped_timer(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            data.append(end_time - start_time)

            return value
        return wrapped_timer
    return wrapper


bubble_times = []
@timer(bubble_times)
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


def v1_r_quick_sort(a):
    l = len(a)
    if l <= 1:
        return a

    p = True
    j = 0
    while p:
        left = []
        right = []
        p = a[l//2-j]
        for i in range(l):
            if a[i] < p:
                left.append(a[i])
            else:
                right.append(a[i])
        
        if len(left) == 0 or len(right) == 0:
            j += 1
        else:
            p = False
    
    return v1_r_quick_sort(left) + v1_r_quick_sort(right)


v1_quick_times = []
@timer(v1_quick_times)
def v1_quick_sort(a):
    return v1_r_quick_sort(a)


def v2_r_quick_sort(a, b, e):
    if b < e: 
        i = b-1
        p = a[e]
    
        for j in range(b, e):
            if a[j] <= p:
                i = i+1
                a[i],a[j] = a[j],a[i]

        a[i+1],a[e] = a[e],a[i+1]

        v2_r_quick_sort(a, b, i)
        v2_r_quick_sort(a, i+2, e)

    return a


v2_quick_times = []
@timer(v2_quick_times)
def v2_quick_sort(a):
    return v2_r_quick_sort(a, 0, len(a)-1)


def v1_build_heap(a, i):
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


v1_heap_times = []
@timer(v1_heap_times)
def v1_heap_sort(a):
    a = [None] + a
    l = len(a)
    b = l//2

    while b > 0:
        v1_build_heap(a, b)
        b -= 1

    i = 1
    while 1 < l-i:
        a[1], a[-i] = a[-i], a[1]
        a = v1_build_heap(a[:-i], 1)+a[l-i:]
        i += 1

    return a[1:]


def v2_build_heap(a, i, mx):
    j = 2*i+1
    while j < mx:
        if a[j] > a[j+1]:
            n = j
        else:
            n = j+1

        if a[i] < a[n]:
            a[i], a[n] = a[n], a[i]
            i = n
            j = 2*i+1
        else:
            break

    if j == mx and a[i] < a[j]:
        a[i], a[j] = a[j], a[i]

    return a


v2_heap_times = []
@timer(v2_heap_times)
def v2_heap_sort(a):
    l = len(a)
    b = l//2

    while b >= 0:
        v2_build_heap(a, b, l-1)
        b -= 1

    i = 0
    while 0 < l-i:
        a[0], a[l-i-1] = a[l-i-1], a[0]
        a = v2_build_heap(a, 0, l-i-2)
        i += 1

    return a


sizes = [1024, 2048, 4096, 8192, 16384]
for size in sizes:
    arr = sample(range(10000000), k=size)
    s = sorted(arr)

    # b = bubble_sort(arr[:])
    # assert b == s, 'Bubble: '+str(b)
    q = v1_quick_sort(arr[:])
    assert q == s, 'Quick v1: '+str(q)
    q = v2_quick_sort(arr[:])
    assert q == s, 'Quick v2: '+str(q)
    # h = v1_heap_sort(arr[:])
    # assert h == s, 'Heap v1: '+str(h)
    h = v2_heap_sort(arr[:])
    assert h == s, 'Heap v2: '+str(h)

start = 10

# b_data = pd.DataFrame({
#     'axis_x': range(start, start+len(sizes)),
#     'axis_y': bubble_times,
# })
# plt.plot('axis_x', 'axis_y', data=b_data, label='Bubble sort', linestyle='-', marker='o')

q1_data = pd.DataFrame({
    'axis_x': range(start, start+len(sizes)),
    'axis_y': v1_quick_times,
})
plt.plot('axis_x', 'axis_y', data=q1_data, label='Quick sort v1', linestyle='-', marker='o')

q2_data = pd.DataFrame({
    'axis_x': range(start, start+len(sizes)),
    'axis_y': v2_quick_times,
})
plt.plot('axis_x', 'axis_y', data=q2_data, label='Quick sort v2', linestyle='-', marker='o')

# h1_data = pd.DataFrame({
#     'axis_x': range(start, start+len(sizes)),
#     'axis_y': v1_heap_times,
# })
# plt.plot('axis_x', 'axis_y', data=h1_data, label='Heap sort v1', linestyle='-', marker='o')

h2_data = pd.DataFrame({
    'axis_x': range(start, start+len(sizes)),
    'axis_y': v2_heap_times,
})
plt.plot('axis_x', 'axis_y', data=h2_data, label='Heap sort v2', linestyle='-', marker='o')

plt.legend(loc='upper left')
plt.show()
