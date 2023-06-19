def solution(n, t, m, p):
    answer = ''
    al=['A','B','C','D','E','F']
    def dd(n, q):
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            if mod>9:
                mod=al[mod-10]
            rev_base += str(mod)

        return rev_base[::-1] 
    
    i=p-1
    game='0'
    for num in range(t * m):
        game += dd(num, n)
    while 1:
        if len(answer) == t:
            break
        answer += game[i]
        i += m
    
    return answer