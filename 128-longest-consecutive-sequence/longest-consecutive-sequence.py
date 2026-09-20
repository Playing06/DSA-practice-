class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        count=0
        for i in nums:
            if i-1 not in nums:
                max_count=1
                while i+max_count in nums:
                    max_count+=1
                count=max(max_count,count)
        return count