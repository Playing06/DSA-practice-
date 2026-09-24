class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        result=[]
        for i in range(len(nums)):
            if nums[i] !=0:
                result.append(nums[i])
        for i in range(len(result)):
            nums[i]=result[i]
        for i in range(len(result),len(nums)):
            nums[i]=0
        return nums

        
        