from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    
    for j in course:
        lst=[]
        for i in orders:
            lst+=list(combinations(sorted(i),j))
    
        counter = Counter(lst)

        if len(counter) != 0 and max(counter.values()) != 1:
                answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)