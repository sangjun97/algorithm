def num(n, a, b):    
    if (n//2 < a and n//2<b):
        a-=n//2
        b-=n//2
        n=n//2
        
    else:
        n=n//2
    return n,a,b
def solution(n,a,b):
    answer = 0
    while True:
        if (n//2 < a and n//2<b) or (n//2>=a and n//2>=b):
            n,a,b=num(n,a,b)
        else:
            return bin(n)[2:].count('0')       
    return answer