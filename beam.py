from fractions import Fraction

def solutions(pegs):
    cp = len(pegs)
    tem = 0
    flag = 1
    for i in reversed(range(cp)[1:]):
        tem = tem + flag * (pegs[i] - pegs[i-1])
        flag = -flag
    # r = 2 * tem / (1 - 2.0 * flag)

    a = (2 * tem)
    b = (1 - 2 * flag)
    r = Fraction(a, b)
    if r < 1:
        return [-1, -1]
    for i in range(cp)[1:]:
        r = pegs[i] - pegs[i-1] - r
        if r < 1:
            return [-1, -1]
    if a % b == 0:
        a = a/b
        b = 1
    return [a, b]


p1 = [4, 17, 50]
p2 = [4, 30, 50, 70, 100, 120]
p3 = [2, 56]
print(solutions(p3))