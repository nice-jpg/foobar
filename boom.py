def solution(x, y):
    return (decrease(int(x), int(y), 0))


def decrease(x, y, c):
    if x == 1 and y == 1:
        return str(c)
    if x < 1 or y < 1:
        return 'impossible'
    xx = max(x, y)
    yy = min(x, y)
    return decrease(yy, xx-yy, c+1)

# print(solution(12345, 1))

def solution1(x, y):
    # Your code here
    xx = min(int(x), int(y))
    yy = max(int(x), int(y))
    c = 0
    while True:
        if xx == 1:
            return str(c + yy - 1)
        if xx == 0:
            return 'impossible'
        t = xx
        c += yy // xx
        xx = yy % xx
        yy = t

print(solution1(11, 2))