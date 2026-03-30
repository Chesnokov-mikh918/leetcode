class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slow = 0;
        int	fast = 0;
        int temp;
        while (fast < nums.size()) {
            if (nums[fast] != val) {
                temp = nums[slow];
                nums[slow] = nums[fast];
                nums[fast] = temp;
                slow++;
            }
            fast++;
        }

        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
	        if (nums[i] != val) {count++;}
        }
        return count;
    }
};