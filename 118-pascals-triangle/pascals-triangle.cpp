class Solution {
public:
    vector<vector<int>> generate(int numRows) {
	    std::vector<std::vector<int>>ans;
	    for (int i = 0; i < numRows;i++) {
		    if (i == 0) {
			    ans.push_back({ 1 });
			    continue;
		    }
            std::vector<int>temp;
            for (int j = 0; j < i + 1; j++) {
                if (j == 0) {
                    temp.push_back(1);
                    continue;
                }
                if (j == i) {
                    temp.push_back(1);
                    continue;
                }
                temp.insert(temp.begin() + j, ans[i - 1][j] + ans[i - 1][j - 1]);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};