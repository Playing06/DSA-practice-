class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        result={}
        for i in nums:
            if i  in result:
                return True
            else:
                result[i]=1
        return False