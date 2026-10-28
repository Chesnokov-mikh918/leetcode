class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def isl_count(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            val = grid[i][j]
            grid[i][j] = 0
            count = val + isl_count(i + 1, j) + isl_count(i - 1, j) + isl_count(i, j - 1) + isl_count(i, j + 1)
            return count

        ans = 0
        for i in range(n):
            for j in range(m):
                count = 0
                if grid[i][j] > 0:
                    count = isl_count(i, j)
                    if count % k == 0:
                        ans += 1
        return ans