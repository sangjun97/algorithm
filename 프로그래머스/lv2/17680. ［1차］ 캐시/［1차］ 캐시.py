def solution(cacheSize, cities):
    answer = 0
    cache=[]
    for i in cities:
        i=i.lower()
        if i not in cache:
            if len(cache)<cacheSize:
                cache.append(i)
                answer+=5
            elif cacheSize==0:
                answer=5*len(cities)
                break
            else:
                cache.pop(0)
                cache.append(i)
                answer+=5
        else:
            x=cache.pop(cache.index(i))
            cache.append(x)
            answer+=1
    return answer
print(solution(3, ["A","B","A"]))