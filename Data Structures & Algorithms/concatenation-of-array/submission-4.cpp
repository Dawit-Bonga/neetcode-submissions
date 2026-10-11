class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> output(2 * nums.size());
        int n = nums.size();
        for (int i = 0; i < nums.size(); ++i ){
            output[i] = nums[i];
            output[i + n] = nums[i];
        }

        return output;
    }
};