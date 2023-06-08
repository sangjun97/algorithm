def solution(n, k):
    answer = 0
    def a(n, q):
        rev_base = ''

        while n > 0:
            n, mod = divmod(n, q)
            rev_base += str(mod)

        return rev_base[::-1] 
    num = a(n,k)
    num=num.split('0')
    for i in num:
        if i not in ['1','']:
            i=int(i)
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    break
            else:
                answer+=1
    return answer 