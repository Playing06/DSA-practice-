class Solution:
    def maximumLength(self, s: str) -> int:
        group=[[] for _ in range(26)]
        count=0
        for i in range(len(s)):
            if i>0 and s[i]== s[i-1]:
                count+=1
            else:
                count=1
            group[ord(s[i])-ord('s')].append(count)
        ans=-1
        for i in group:
            i.sort(reverse=True)
            if len(i)>=3:
                ans=max(ans,i[2])
        return ans
        
        