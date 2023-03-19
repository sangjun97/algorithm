def solution(n):
    b=[0,1]
    for i in range(2, n+1):
        b.append((b[i-1]+b[i-2])%1234567)
    return b[-1]