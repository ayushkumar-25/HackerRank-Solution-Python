# Method-1
str = input()
print(any (x.isalnum() for x in str))
print(any (x.isalpha() for x in str))
print(any (x.isdigit() for x in str))
print(any (x.islower() for x in str))
print(any (x.isupper() for x in str))

# Method-2
str = input()
for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print(any(eval('x.' + test + '()') for x in str))

# Method-3
s = input()
for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
    print(len(list(filter(lambda c: eval('c.' + test + '()'), list(s)))) > 0)