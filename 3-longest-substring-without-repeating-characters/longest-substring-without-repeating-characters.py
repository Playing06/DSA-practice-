class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=set()
        count=0
        max_count=0
        for i in range(len(s)):
            while s[i] in result:
                result.remove(s[count])
                count+=1
            result.add(s[i])
            max_count=max(max_count,i-count+1)
        return max_count
            
        

