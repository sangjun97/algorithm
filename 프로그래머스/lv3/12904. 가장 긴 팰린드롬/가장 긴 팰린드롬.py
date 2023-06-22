def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            n = s[i:j]
            if n==n[::-1]:
                answer=max(answer,len(n))
    return answer