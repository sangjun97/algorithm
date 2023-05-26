from itertools import permutations
def solution(k, dungeons):
    clears = []
    dungeons_permutaions = list(permutations(dungeons, len(dungeons)))

    for case in dungeons_permutaions:
        clear = 0
        stamina = k
        
        for dungeon in case:
            if stamina >= dungeon[0]:
                stamina -= dungeon[1]
                clear += 1

        clears.append(clear)
    return max(clears)