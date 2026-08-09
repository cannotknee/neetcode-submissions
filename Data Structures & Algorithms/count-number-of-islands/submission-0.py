class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count

# number of islands
# DFS
# recursively call and mark seen
# dictionary
# current element 0 or 1
# when out of bounds or 0
# how to track the number of islands??? how to mark all elements on the same island in a group, so that when we revisit, we skip?