class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std::string longest{};
        int min_len = strs[0].size();

        for (const string& s : strs) {
            min_len = min(min_len, (int)s.size());
        }

        for (int i = 0; i < min_len; ++i){
            char curr = strs[0][i];

            for (const string& s: strs){
                if (curr != s[i]){
                    return s.substr(0,i);
                }
            }
        }

        return strs[0].substr(0,min_len);
    }
};