def solution(my_string):
    answer = ''
    a=['a','e','i','o','u']
    for i in my_string:
        cnt=0
        for j in a:
            if i!=j:
                cnt+=1
        print(cnt)
        if cnt==len(a):
            answer+=i
            print(i)
    return answer