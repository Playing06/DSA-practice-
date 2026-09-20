class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive=[]
        negative=[]
        for i in nums:
            if i>=0:
                positive.append(i)
            if i<0:
                negative.append(i)
        result=[]
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result
        