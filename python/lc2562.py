class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
         result = 0
         while len(nums)>0:
             if len(nums)>1:
                 num1 = nums[0]
                 num2 = nums[-1]
                 con = int(str(num1)+str(num2))
                 result = result + con
                 del nums[0]
                 del nums[-1]
             else:
                 result = result + nums[0]
                 del nums[0]
         return result

