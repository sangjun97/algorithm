def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw==i:
            answer='login'
            return answer
        elif id_pw[0]==i[0]:
            if answer=='login':
                pass
            else:
                answer='wrong pw'
        else:
            if answer=='login' or answer=='wrong pw':
                continue
            else:
                answer='fail'
            
    return answer