import re
def solution(str1, str2):
    answer = 0
    a=[]
    b=[]
    c=[]
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            a.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            b.append(str2[i:i+2].lower())
    if len(set(a+b))==0:
           return 65536
    for i in a:
        if i in b:
            b.remove(i)
            c.append(i)
    num1=len(c)
    num2=len(a)+len(b)
    answer=int(num1/num2*65536)

    return answer