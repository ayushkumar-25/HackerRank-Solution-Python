# Method-1 (without list comprehension)
def swap_case(s):
    for i in s:
        if (i>='A' and i<='Z'):
            print(i.lower(),end="")
        elif (i>='a' and i<='z'):
            print(i.upper(),end="")
        else:
            print(i,end="")
    return("")

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# Method-2 (with list comprehension)
def swap_cases(s):
    
    return ''.join([c.upper() if c.islower() else c.lower() for c in s])

if __name__ == '__main__':
    s = input()
    result = swap_cases(s)
    print(result)