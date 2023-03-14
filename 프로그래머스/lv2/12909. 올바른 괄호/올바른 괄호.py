def solution(s):
    answer = True
    a=0
    b=0
    if s[0]==')':
        return False
    else:
        for i in s:
            if i=='(':
                a+=1
            else:
                b+=1
            if a<b:
                return False
    if a!=b:
        return False

    return True