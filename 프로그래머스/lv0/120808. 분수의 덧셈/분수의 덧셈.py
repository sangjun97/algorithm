import math
def solution(denum1,num1,denum2,num2):
    num=num1*num2
    denum=denum1*num2+denum2*num1
    n=math.gcd(num,denum)
    if n==1:
        answer=[denum,num]
    else:
        answer=[denum/n,num/n]
    return answer
