import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = dict()
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for j in freq:
            heapq.heappush(heap, (-freq[j], j))

        ans = []
        for l in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans