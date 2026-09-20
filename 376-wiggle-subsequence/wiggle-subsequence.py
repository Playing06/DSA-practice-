class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if len(nums)<2:
            print(len(nums))
        pos=1
        neg=1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                pos=neg+1
            elif nums[i+1]<nums[i]:
                neg=pos+1
        return max(pos,neg)
        