class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            elif i > n:
                return 0
            memo[i] = dfs(i + 1) + dfs(i + 2)
            return memo[i]
        return dfs(0)
# distinct ways to climb stairs
# DP / DFS
# state: i (current step)
# stops only when i == n else invalid path
# explores in either 1 or 2 step
# how do i count the number of unique solutions?