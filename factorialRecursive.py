"""
********************************************
* This is a program to print the factorial *
********************************************
"""
print(__doc__, "\n")


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


a = int(input("Enter a number to evaluate its factorial: "))
value = fact(a)
print("Factorial of {} is: {}".format(a, value))
