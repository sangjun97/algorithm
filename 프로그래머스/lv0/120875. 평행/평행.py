def solution(dots):
    answer = 0
    dd=dots[:]

    for i in range(1,4):
        print(dots)
        print(i)
        a=dots[0][0]-dots[i][0]
        b=dots[0][1]-dots[i][1]
        del dots[i]
        del dots[0]
        c=abs(b/a)
        e=dots[0][0]-dots[1][0]
        f=dots[0][1]-dots[1][1]
        g=abs(f/e)
        dots=dd[:]
        if c==g:
            answer=1
        
        
    return answer