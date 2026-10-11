class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<string>> nameToGroup;

        for (auto str: strs){
            std::string curr = str;

            std::sort(curr.begin(), curr.end());
            nameToGroup[curr].push_back(str);
        }

        std::vector<vector<string>> finalOutput;

        for (auto const& [group, members]: nameToGroup){
            finalOutput.push_back(members);
        }

        return finalOutput;

    }
};
