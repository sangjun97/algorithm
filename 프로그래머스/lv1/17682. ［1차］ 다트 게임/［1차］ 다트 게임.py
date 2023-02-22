def solution(dartResult):
    answer = 0 
    a=[]
    b= ''
    for i in dartResult:
        
        if i.isalpha():
            if i == 'S':
                a.append(int(b))
            elif i == 'D':
                a.append(int(b)**2)
            else:
                a.append(int(b)**3)
            b=''
        elif i.isdigit():
            b+=i
        else:
            if i=='*':
                a[-1]=a[-1]*2
                try:
                    a[-2]=a[-2]*2
                except:
                    pass
            else:
                a[-1]=-a[-1]
    answer=sum(a)
    return answer