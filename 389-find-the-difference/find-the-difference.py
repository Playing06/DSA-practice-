class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # result=[]
        # for i in t:
        #     if t.count(i)> s.count(i):
        #         result.append(i)
        #         t.replace(i,"",1)
        #         break
        # return "".join(result)
        count={}
        for i in s:
            count[i]=count.get(i,0)+1
        for i in t:
            if i not in count or count[i]==0:
                return i
                break
            count[i]-=1