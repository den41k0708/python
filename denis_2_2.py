import math
import time

def radical(n):
    if (n == 1):
        return 1
    return (n + radical(n - 1)) ** (0.5)

def factorial(x, step):
    if type(x) == int and type(step) == int and x >= 0 and step >= 0:
        result = lambda x: result(x - step) * x if x - step > 0 else x
        if x == 0:
            x = 1
        return result(x)
    else:
        raise TypeError("The given value must be positive integer")


n = 10
m = 10
print(radical(n)/factorial(m, 2))

time.sleep(5)
