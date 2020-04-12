l, n = input().split()

n = int(n)
l = int(l)
from functools import reduce

list1 = []
b = []
for i in range(l):
    a = list(map(int, input().split()))
    list1.append(a)
# print(list1)

for i in range(l):
    b.append(max(list1[i]))
# print(b)
b = list(map(lambda x: x ** 2, b))
# print(b)
value = reduce(lambda x, y: x + y, b)
print(value % n)
