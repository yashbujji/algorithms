class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        res = []
        for num in nums:
            res.append(total_prod)
            total_prod *= num
        
        total_prod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= total_prod
            total_prod *= nums[i]
        
        return res