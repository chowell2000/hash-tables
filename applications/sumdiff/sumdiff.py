"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

def symdif(q):
    sums = dict()
    diffs = dict()
    symmdiffs = dict()
    for x in q:
        for y in q:
            sums[(x,y)] = f(x) + f(y)
            diffs[(x,y)] = f(x) - f(y)


    for i in sums.keys():
        for j in diffs.keys():
            if sums[i] == diffs[j]:
                symmdiffs[i,j] = sums[i]

    return symmdiffs

# print(symdif(q))
for i in symdif(q).keys():
    print(f'f({i[0][0]}) + f({i[0][1]}) = f({i[1][0]}) - f({i[1][1]})  =  {symdif(q)[i]}  '
          f'=  {f(i[0][0])} + {f(i[0][1])} = {f(i[1][0])} - {f(i[1][1])}')

