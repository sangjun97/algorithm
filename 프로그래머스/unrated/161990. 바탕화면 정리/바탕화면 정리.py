def solution(wallpaper):
    answer = []
    a=dict()
    for i, j in enumerate(wallpaper):
        if '#' in j:
            a[i]=list(filter(lambda e:j[e] == '#', range(len(j))))
    answer=[min(a.keys()),min(map(min,a.values())),max(a.keys())+1,max(map(max,a.values()))+1]
    return answer