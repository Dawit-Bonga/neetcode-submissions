class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        test = [0] * k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False

        def dfs(i):
            if i >= len(nums):
                return all(s == target for s in test)
            
            for j in range(k):
                if j > 0 and test[j] == test[j - 1]:
                    continue
                if test[j] + nums[i] > target:
                    continue
                
                test[j] += nums[i]
                if dfs(i + 1):
                    return True
                test[j] -= nums[i]
            
            return False
        
        return dfs(0)
        
            
        