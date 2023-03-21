def solution(s):
    a=[]
    s=list(s)
    for i in range(len(s)):
        if not a:
            a.append(s[i])
        else:
            if a[-1]==s[i]:
                a.pop()
            else:
                a.append(s[i])
    if a:
        return 0

    return 1