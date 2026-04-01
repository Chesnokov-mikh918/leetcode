class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_val = -1;
        int left = 0;
        int right = height.size() - 1;
        while (left <= right) {
            max_val = std::max(max_val, std::min(height[left], height[right]) * (right -left));
            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }
        return max_val;
    }
};