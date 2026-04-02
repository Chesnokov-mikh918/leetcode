class Solution {
public:
    int findLHS(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int left = 0;
        int right = -1;
        int max_len = 0;
        while (left < nums.size()) {
            while (right + 1 < nums.size() && ((nums[right + 1] - nums[left]) <= 1)) {
                if ((nums[right + 1] - nums[left]) == 1) {
                    max_len = std::max(max_len, right + 2 - left);
                }
                right++;
            }
            left++;
        }
        return max_len;
    }
};