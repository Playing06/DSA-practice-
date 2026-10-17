class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # pow=0
        # while n>=3**pow:
        #     if 3**pow==n:
        #         return True
        #     pow+=1
        # return False
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1
