"""

找出1000以内的所有完数

"""

import numpy as np

def find_fac(num):
    fac_set = []
    for i in range(1, num):
        if num % i == 0:
            fac_set.append(i)
    fac_set = np.array((fac_set))
    return np.sort(fac_set)

for i in range(1, 1001):
    num_arr = find_fac(i)
    if np.sum(num_arr) == i:
        print(i, end = ' ')

