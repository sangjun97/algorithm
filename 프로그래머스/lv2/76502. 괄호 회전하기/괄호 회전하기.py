from collections import deque
def solution(s):
    answer = 0
    lst=['[]','{}','()']
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1)
        a=deque()
        for j in s:
            if a:
                if a[-1]=='[' and j==']':
                    a.pop()
                elif a[-1]=='(' and j==')':
                    a.pop()
                elif a[-1]=='{' and j=='}':
                    a.pop()
                else:
                    a.append(j)
            else:
                a.append(j)
        if len(a)==0:
            answer+=1

    return answer