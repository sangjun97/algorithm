from collections import deque
def solution(operations):
    answer = [0,0]
    dd=deque()
    for i in operations:
        if i=='D 1' and dd:
            dd.remove(max(dd))
        elif i=='D -1' and dd:
            dd.remove(min(dd))
        elif i[0]=='I':
            dd.append(int(i[2:]))
    if dd:
        dd=sorted(dd)
        return [dd[-1],dd[0]]
    return answer