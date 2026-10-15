class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n<0:
            
            n=-n
            return 1.0/self.myPositive(x,n)
        return self.myPositive(x,n)
        
    def myPositive(self,x: float, n: int) -> float:
        result= 1.0
        while n>0:
            if n % 2==1:
                result =result*x
            x=x*x
            n=n//2
        return result