def solution(w,h):
    answer = 1
    num=0
    for i in reversed(range(2,min(w,h)+1)):
        if w%i==0 and h%i==0:
            num=i
            break
    if num:
        return w*h-(w+h-num)
    else:
        return w*h-(w+h-1)
    