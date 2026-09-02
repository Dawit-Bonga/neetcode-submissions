class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {} # index to longets subsequence
        n = len(nums)
        def dfs(i):
            if i == n:
                return 0
            
            if (i) in cache:
                return cache[i]
            
            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            
            cache[i] = best
            return best
        
        final = 0
        for i in range(n):
            final = max(final, dfs(i))
            
        return final

