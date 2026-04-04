class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        std::unordered_map<std::string, int>data;
        std::unordered_set<std::string>pre_ans; 
        std::vector<std::string>ans;
        std::string temp;

        for (int i = 0; i < 10; i++) {
            temp += s[i];
        }

        data[temp]++;
        for (int i = 10; i < s.length(); i++) {
            temp = temp.substr(1, temp.length());
            temp += s[i];
            if (data[temp] >= 1) {
                pre_ans.insert(temp);
            }
            else {
                data[temp]++;
            }
        }

        for (auto& iter : pre_ans) {
	        ans.push_back(iter);
        }

        return ans;
    }
};