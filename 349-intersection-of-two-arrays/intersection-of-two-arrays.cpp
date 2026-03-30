class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int>ans;
        std::unordered_set<int>check;
        std::sort(nums1.begin(), nums1.end());
        std::sort(nums2.begin(), nums2.end());
        int p1 = 0;
        int p2 = 0;
        while (p1 < nums1.size() && p2 < nums2.size()) {
            if (nums1[p1] == nums2[p2]) {
                if (check.count(nums1[p1]) == 0) {
                    ans.push_back(nums1[p1]);
                    check.insert(nums1[p1]);
                    p1++;
                    p2++;
                }
                else {
                    p1++;
                    p2++;
                }
            }
            else if (nums1[p1] < nums2[p2]) {
                p1++;
            }
            else {
                p2++;
            }
        }
        return ans;
    }
};