import math
import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def sum_e(x, a, e):
    k, sum_old = 1, 0
    sum_new = (math.cos(x ** k) + math.sin(a ** k)) / factorial(2*k - 1)
    while math.fabs(sum_old - sum_new) >= e:
        k, sum_old = k + 1, sum_new
        sum_new = (math.cos(x ** k) + math.sin(a ** k)) / factorial(2*k - 1)
    return sum_new, k



x = float(input("enter x: "))
a = float(input("enter a: "))
e = float(input("enter e: "))

sum_e, k = sum_e(x, a, e)
print("step 12" + str(k) + " = " + str(sum_e))

time.sleep(5)
