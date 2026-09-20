class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        ans=special[0]-bottom
        for i in range(1,len(special)):
            gap=special[i]-special[i-1]-1
            ans=max(gap,ans)
        ans=max(ans,top-special[-1])
        return ans
