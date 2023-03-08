def solution(keymap, targets):
    answer = []
    for i in targets:
        a=0
        for j in i:
            mim=99999
            # print('j',j)
            for k in keymap:
                try:
                    mim=min(k.index(j)+1,mim)
                except:
                    pass
            # print('mim',mim)
            a+=mim
        if a>=99999:
            a=-1
        answer.append(a)
    return answer
print(solution(keymap = {"ABCDE","ABBCE"}, targets={"ABBEF"}))