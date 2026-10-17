class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pow=0
        while n>=3**pow:
            if 3**pow==n:
                return True
            pow+=1
        return False
