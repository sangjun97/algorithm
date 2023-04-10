from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque(bridge_length*[0])
    weights = deque(truck_weights)
    bridge_sum=0
    while len(bridge):
        answer+=1
        bridge_sum += bridge[-1] 
        bridge_sum -= bridge[0] 
        bridge.popleft()
               
        if weights:
            if bridge_sum+weights[0] <= weight:
                bridge.append(weights.popleft())
            else:
                bridge.append(0)
    return answer