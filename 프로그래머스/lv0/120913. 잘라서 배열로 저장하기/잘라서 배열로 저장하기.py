def solution(my_str, n):
    answer = []
    cnt=0
    a=''
    for i in my_str:
        if cnt!=n-1:
            a+=i
            cnt+=1
        else:
            a+=i
            answer.append(a)
            cnt=0
            a=''
    if len(my_str)%n!=0:
        answer.append(a)
    return answer