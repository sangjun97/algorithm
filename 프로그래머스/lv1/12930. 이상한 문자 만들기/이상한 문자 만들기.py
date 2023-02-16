def solution(s):
    answer = ''
    a=0
    for i in range(len(s)):
        if s[i]==' ':
            answer+=' '
            a=0
        elif a%2==0:
            answer+=s[i].upper()
            a+=1
        else:
            answer+=s[i].lower()
            a+=1
    return answer