class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.subset(target, candidates, [], 0, res)
        return res

    def subset(self, target, candidates, temp, l, res):
        if target < 0 or l>len(candidates)-1:
            return
        elif target == 0:
            temp = sorted(temp,key = lambda x:x)
            if temp not in res:
                res.append(temp)
            return
        else:
            #for i in range(l,len(candidates)):
            self.subset(target-candidates[l], candidates,temp+[candidates[l]],l, res)
            self.subset(target,candidates,temp,l+1, res)
                #self.subset(target-candidates[i], candidates,temp+[candidates[i]],l, res)