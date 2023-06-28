def solution(n, s):
    answer = []
    if n>s:
        return [-1]
    i = s//n
    j = s%n
    answer=[i]*n
    for i in range(j):
        answer[-1-i]+=1
    return answer