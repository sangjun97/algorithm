def solution(polynomial):
    answer = ''
    polynomial=polynomial.split(' + ')
    a=0
    b=0
    for i in polynomial:
        if i.isdigit():
            a+=int(i)
        else:
            if i=='x':
                b+=1
            else:
                b+=int(i[:-1])
    if b==1:
        b=''
    if a!=0 and b!=0:
        answer=f'{b}x + {a}'
    elif a==0:
        answer=f'{b}x'
    elif b==0:
        answer=f'{a}'
    else:
        answer=f'0'
    print(answer)
    return answer