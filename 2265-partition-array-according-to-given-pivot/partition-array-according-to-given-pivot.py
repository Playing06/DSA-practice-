class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        low=[]
        midd=[]
        high=[]
        for i in nums:
            if i<pivot:
                low.append(i)
            elif i==pivot:
                midd.append(i)
            elif i>pivot:
                high.append(i)
        return low+midd+high
                

