class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        result=[0]*len(nums)
        even=0
        odd=1
        for i in range(len(nums)):
            if nums[i]%2==0:
                result[even]=nums[i]
                even+=2
            else:
                result[odd]=nums[i]
                odd+=2
        return result
        