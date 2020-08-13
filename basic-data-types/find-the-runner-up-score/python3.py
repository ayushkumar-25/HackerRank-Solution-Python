if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    l1 = set(arr)
    l2 = list(l1)
l2.sort()
print(l2[-2])