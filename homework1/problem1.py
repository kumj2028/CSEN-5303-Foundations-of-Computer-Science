import math

def find_largest_dif(list):
    n = len(list)
    max_dif = -math.inf
    for i in range(n - 1):
        dif = list[i + 1] - list[i]
        if dif > max_dif:
            max_dif = dif
    return max_dif