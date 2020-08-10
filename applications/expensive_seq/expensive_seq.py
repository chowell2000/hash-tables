# Your code here
#
# exps(x, y, z) =
#      if x <= 0: y + z
#      if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

exps = dict()

# for x in range(404):
#     for y in range(10000):
#         num = x + y
#         exps[(0,x,y)] = num
#         exps[(-1,x,y)] = num
#         exps[(-2,x,y)] = num
        # exps[(1,x,y)] = num * 3

# for x in range(1, 151):
#     for y in range(401):
#         for z in range(2401):
#             num = exps[(x-1, y + 1, z)] + exps[(x-2,y+2,z*2)] + exps[(x-3, y+3, z*3)]
#             exps[(x,y,z)] = num


def exp_s(x,y,z):
    if (x,y,z) in exps.keys():

        return exps[(x,y,z)]
    else:
        if x <= 0:
            exps[(x,y,z)] = y + z
            return y + z
        num1 = exp_s(x-1,y+1, z)
        num2 = exp_s(x-2,y+2,z*2)
        num3 =exp_s(x-3, y+3, z*3)
        num = num1 + num2 + num3
        exps[(x,y,z)] = num
        # print(num)
        return num


def expensive_seq(x, y, z):
    # Your code here
    if (x,y,z) in exps.keys():

        return exps[(x,y,z)]
    else:
        exp_s(x,y,z)
        return exps[(x,y,z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
