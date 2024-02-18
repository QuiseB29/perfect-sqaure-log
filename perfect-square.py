# Given a number, determine if it's a perfect square (like 1, 4, 9, 16, …).

from math import sqrt

def check_ps(number):
    if sqrt(number) - int(sqrt(number)):
        return False
    return True

n = int(input("Enter a number"))
flag = check_ps(n)
if flag:
    print(f"{n} is perfect sqaure")
else:
    print(f"{n} is not a square")