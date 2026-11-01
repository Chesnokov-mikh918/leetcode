class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 1

        for i in range(n):
            for j in range(m):
                left, top = dp[i][j][0], dp[i][j][1]
                if grid[i][j] == 0:
                    to_right = to_down = left + top
                else:
                    to_right, to_down = top, left
                
                if j + 1 < m:
                    dp[i][j + 1][0] = (dp[i][j + 1][0] + to_right) % (10**9 + 7)
                if i + 1 < n:
                    dp[i + 1][j][1] = (dp[i + 1][j][1] + to_down) % (10**9 + 7)

        return sum(dp[n - 1][m - 1]) % (10**9 + 7)