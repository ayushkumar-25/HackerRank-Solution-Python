#!/bin/python3

import sys

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    sum = 0
    for i in range(1, n):

        if (i % 3 == 0 or i % 5 == 0):
            sum = sum + i
        else:
            sum = sum
    print(sum)