class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        largest_arr = {}
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                largest_arr[nums2[i]] = stack[-1]
            else:
                largest_arr[nums2[i]] = -1
            stack.append(nums2[i])
        return [largest_arr[num] for num in nums1]
