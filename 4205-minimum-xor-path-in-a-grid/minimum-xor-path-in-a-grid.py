class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        pos_vals = n * [m * [0]]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    pos_vals[i][j] = {grid[i][j]}
                elif i == 0:
                    pos_vals[i][j] = {x ^ grid[i][j] for x in pos_vals[i][j - 1]}
                elif j == 0:
                    pos_vals[i][j] = {x ^ grid[i][j] for x in pos_vals[i - 1][j]}
                else:
                    t1 = {x ^ grid[i][j] for x in pos_vals[i - 1][j]}
                    t2 = {x ^ grid[i][j] for x in pos_vals[i][j - 1]}
                    pos_vals[i][j] = t1 | t2
        return min(pos_vals[n - 1][m - 1])
