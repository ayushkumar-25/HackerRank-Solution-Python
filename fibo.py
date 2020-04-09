k = int(input("Enter number of test case: "))
a, b, c, sum1 = 0, 1, 0, 0
for _ in range(k):
    n = int(input("Enter Number: "))
    for i in range(1, n):
        if a % 2 == 0:
            if a > n:
                break
            sum1 = sum1 + a

        c = a + b
        a = b
        b = c
    print(sum1)
