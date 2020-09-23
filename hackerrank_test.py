import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    #seperating every character of string and forming a list
    list1 = []
    for i in s:
        list1.append(i)

    result = []
    for i in list1:
        if i == 'U':
            result.append(1)




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
