# Your code here
import random
import math

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

vs = [[]]*15

for x in range(0,15):
    vs[x] = [((x**y)!) for y in range(1,6)]

# factorials = [1]*300000
#
# for x in range(1,300000):
#     factorials[x] = factorials[x-1] * x

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    v = powers[x][y -1]
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v
    # return


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

# print(powers)
#
# for x in range(20):
#     print(factorials[x])