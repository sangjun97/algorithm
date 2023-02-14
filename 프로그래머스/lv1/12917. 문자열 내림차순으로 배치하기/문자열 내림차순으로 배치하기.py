def solution(s):
    answer = ''
    up=[]
    for i in s:
        if i.isupper():
            up.append(i)
            s=s.replace(i,'')
    answer=''.join(sorted(s,reverse=True)+sorted(up,reverse=True))
    return answer