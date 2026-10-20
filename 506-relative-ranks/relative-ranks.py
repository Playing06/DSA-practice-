class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sort_score=sorted(score,reverse=True)
        rank={}
        for i,value in enumerate(sort_score,1):      
            if i==1:
                rank[value]="Gold Medal"
            if i==2:
                rank[value]="Silver Medal"
            if i==3:
                rank[value]="Bronze Medal"
            if i>3:
                rank[value]=str(i)
        result=[]
        for i in score:
            result.append(rank[i])
        return result
        