class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_sum=0
        min_sum=0
        current_max=0
        current_min=0
        for i in nums:
            current_max+=i
            current_min+=i
            if current_max<0:
                current_max=0
            if current_min>0:
                current_min=0
            max_sum=max(max_sum,current_max)
            min_sum=min(min_sum,current_min)
        return max(max_sum,abs(min_sum))
        