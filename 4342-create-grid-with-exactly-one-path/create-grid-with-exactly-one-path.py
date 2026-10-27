class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = m * ['']
        for i in range(m):
            for j in range(n):
                if i == 0 or j == (n - 1):
                    grid[i] += '.'
                else:
                    grid[i] += '#'
        return grid