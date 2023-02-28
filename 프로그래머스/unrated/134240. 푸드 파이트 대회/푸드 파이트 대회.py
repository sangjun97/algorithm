def solution(food):
    answer = ''
    a=[]
    for i in range(1, len(food)):
        a.append(str(i)*(food[i]//2))
    answer=''.join(a+['0']+a[::-1])

    if answer=='0':
        return ''
                   
    return answer