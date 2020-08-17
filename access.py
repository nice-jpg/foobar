

def solution(l):
    # Your code here
    l.sort()
    x = []
    y = {}
    count = 0
    for li in l:
        for yi in y:
            if li % yi == 0:
                count += y[yi]
        for xi in x:
            if li % xi == 0:
                y[li] = y.get(li, 0) + 1
        x.append(li)
    return count


l1 = [1, 1, 1]
l2 = [1, 2, 3, 4, 5, 6]
l3 = [6, 6, 6, 12, 18]
l4 = [1, 3, 5, 7]
l5 = [6, 5, 4, 3, 2, 1]
l6 = [1, 1, 1, 1]

print(solution(l6))
