class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(0,len(nums),2):
            min_num=min(nums[i],nums[i+1])
            count+=min_num
        return count