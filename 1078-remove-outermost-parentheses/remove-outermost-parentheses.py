class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count=0
        result=[]
        for i in range (len(s)):
            if s[i]=="(" :
                if count>0:
                    result.append(s[i])
                count+=1
            else:
                count-=1
                if count>0:
                    result.append(s[i])
        return ''.join(result)
