# at each stage, there is two way to go up, either one stair or two stair
def stairs(n):
    dp = [ 0  for i in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(n):
        dp[i] = dp[i-2] + dp[i-1]

    return dp[n-1]


print(stairs(3))