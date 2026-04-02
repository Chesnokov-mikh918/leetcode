class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        std::unordered_map<int, int>means;
        int slow = 0;
        int fast = 0;
        int temp;
        while (fast < nums.size()) {
            if (means[nums[fast]] > 1) {
                fast++;
            }
            else {
                means[nums[fast]]++;
                temp = nums[slow];
                nums[slow] = nums[fast];
                nums[fast] = temp;
                slow++;
                fast++;
            }
        }
        return slow;
    }
};