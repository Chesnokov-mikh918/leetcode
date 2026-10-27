class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # закрашивание единого острова единицами
        def dfs(i, j):
            if i >= n or i < 0 or j >= m or j < 0 or grid[i][j] == 1:
                return
            grid[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        # края в любом случае невалидные так что закрасим 1
        for i in range(n):
            for j in range(m):
                if i == 0 or i == (n - 1) or j == 0 or j == (m - 1):
                    dfs(i, j)
        # основной проход
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    count += 1
                    dfs(i, j)
        return count