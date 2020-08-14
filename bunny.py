

def check(l, step, selected, count):
    if len(selected) == count:
        if (sum(l) - sum(selected)) % 3 == 0:
            ll = l[:]
            for si in selected:
                ll.remove(si)
            return ll
    if step >= len(l):
        return
    selected.append(l[step])
    res = check(l, step + 1, selected, count)
    if res:
        return res
    selected.pop()
    return check(l, step + 1, selected, count)




def solution(l):
    l.sort()
    for c in range(len(l)):
        res = check(l, 0, [], c)
        if res:
            r = ''
            for ri in reversed(res):
                r += str(ri)
            return int(r)
    return 0



l1 = [3, 1, 4, 1]
l2 = [3, 1, 4, 1, 5, 9]
l3 = [1, 1, 2, 3]
print(solution(l1))

