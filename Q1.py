class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        indegree={}
        for s,e in edges:
            if s not in indegree:
                indegree[s]=1
            else:
                indegree[s]+=1
            if e not in indegree:
                indegree[e]=1
            else:
                indegree[e]+=1
        for key,value in indegree.items():
            if value>1:
                return key