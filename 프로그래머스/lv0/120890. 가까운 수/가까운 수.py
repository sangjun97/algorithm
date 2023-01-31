def solution(array, n):
    answer = 0
    a=[]
    array=sorted(array)
    for i in array:
        a.append(abs(n-i))
    print(a.index(min(a)))
    answer=array[a.index(min(a))]
    return answer