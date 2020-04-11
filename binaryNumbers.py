# Day 10 of "30 Days of Code"

'''n = int(input())
n = bin(n)
n = list(n)
del n[0:2]
print(n)'''
from itertools import count

n = input()
a = n.count('1')
print("The number is between", a)
