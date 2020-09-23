import math
import os
import random
import re
import sys

n = int(input())
ar = list(map(int, input().split()))
result = []


def sock_merchant(n, ar):
    ar.sort()
    for i in ar:
        if ar.count(i) > 1:
            count = ar.count(i)
            no_of_pairs = int(count / 2)
            result.append(no_of_pairs)

            def remove_values_from_list(the_list, val):
                return [value for value in the_list if value != val]

            ar = remove_values_from_list(ar, i)
    return sum(result)


final = sock_merchant(n, ar)
print(final)
