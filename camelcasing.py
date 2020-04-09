"""HackerRank program for camel casing
Input - ayushKumarSingh
Output - 3 (number of words in the input)
"""

s = input()
s = list(s)
sum1 = 0
for i in range(len(s)):
    if (s[i] >= 'A' and s[i] <= 'Z'):
        sum1 += 1
print(sum1 + 1)
