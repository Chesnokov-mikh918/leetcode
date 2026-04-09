class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::string>strs_sort = strs;
        std::vector<std::vector<std::string>>final_ans;
        for (int i = 0; i < strs_sort.size(); i++) {
            std::sort(strs_sort[i].begin(), strs_sort[i].end());
        }

        std::unordered_map<std::string, std::vector<std::string>>ans;

        for (int i = 0; i < strs_sort.size(); i++) {
            ans[strs_sort[i]].push_back(strs[i]);
        }

        for (auto& iter : ans) {
            final_ans.push_back(iter.second);
        }
        
        return final_ans;
    }
};