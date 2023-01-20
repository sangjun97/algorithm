def solution(chicken):
    answer = -1
    a=chicken
    cnt=0
    b=0
    while a//10!=0:
        b=a%10
        a=a//10
        cnt+=a
        a=a+b
        
        print(a)
        
        print('cnt',cnt,'\n')
    print(a)
    answer=cnt
    return answer