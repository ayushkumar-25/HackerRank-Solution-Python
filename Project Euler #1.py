#!/bin/python3


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    sum1 = 0
    for i in range(1, n):

        if i % 3 == 0 or i % 5 == 0:
            sum1 = sum1 + i
        else:
            sum1 = sum1
    print(sum1)
