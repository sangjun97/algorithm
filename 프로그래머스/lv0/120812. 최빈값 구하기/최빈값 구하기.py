def solution(array):
    max_=0
    num=0
    a=set(array)
    for i in a:
        if max_<array.count(i):
            max_=array.count(i)
            num=i
        elif max_==array.count(i):
            num=-1
    answer=num
    return answer