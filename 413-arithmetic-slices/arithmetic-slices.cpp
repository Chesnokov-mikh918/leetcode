class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        if (nums.size() < 3) {
            return 0;
        }
        for (int i = nums.size() - 1; i > 0; i--) {
            nums[i] = nums[i] - nums[i - 1];
        }
        nums.erase(nums.begin());

        int left = 0;
        int count, all_count = 0;
        for (int right = 1; right < nums.size(); right++) {
            if (nums[right] != nums[right - 1]) {
                count = right - left;
                if (count >= 2) {
                    all_count += (count * (count - 1)) / 2;
                }
                left = right;
            }
        }

        count = nums.size() - left;
        if (count >= 2) {
            all_count += (count * (count - 1)) / 2;
        }

	    return all_count;
    }
};