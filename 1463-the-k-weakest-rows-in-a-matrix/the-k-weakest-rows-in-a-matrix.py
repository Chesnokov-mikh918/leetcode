import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(0, len(mat)):
            sum_i = sum(mat[i])
            heapq.heappush(heap, (sum_i, i))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res