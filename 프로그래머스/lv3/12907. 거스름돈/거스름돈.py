def solution(n, money):
    answer = 0
    dp=[1]+[0]*n
    for m in money:
        for i in range(m,n+1):
            if i>=m:
                dp[i]=dp[i]+dp[i-m]
    return dp[n]%1_000_000_007