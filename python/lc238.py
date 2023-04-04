class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        result = []
        for num in nums:
            result.append(total_prod)
            total_prod *= num
        
        total_prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= total_prod
            total_prod *= nums[i]
        
        return result