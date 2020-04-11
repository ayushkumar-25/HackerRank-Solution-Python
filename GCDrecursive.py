def gcd(x, y):
    rem = x % y
    if rem == 0:
        return y
    else:
        return gcd(y, rem)


a = int(input("Enter the 1st value: "))
b = int(input("Enter the 2nd value: "))
print("GCD of {} and {} is {}".format(a, b, gcd(a, b)))