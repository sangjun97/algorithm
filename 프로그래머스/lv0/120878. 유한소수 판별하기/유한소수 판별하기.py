import math
def solution(a, b):
    answer = 1
    c=a/math.gcd(a,b)
    d=b/math.gcd(a,b)
    if len(str(c/d))>=16:
        answer=2
    return answer