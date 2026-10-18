class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # result={}
        # for i in nums:
        #     if i  in result:
                
        #         result[i]+=1
        #     else:
        #         result[i]=1
        # return max(result,key=result.get)
        node=None
        count=0
        for i in nums:
            if count==0:
                node=i
            if node==i:
                count+=1
            else:
                count-=1
        return node