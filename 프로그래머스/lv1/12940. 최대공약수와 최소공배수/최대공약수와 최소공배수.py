from math import gcd
def solution(n, m):
    def lcm(x,y):
        return x*y//gcd(x,y)
    answer = [gcd(n,m),lcm(n,m)]
    return answer