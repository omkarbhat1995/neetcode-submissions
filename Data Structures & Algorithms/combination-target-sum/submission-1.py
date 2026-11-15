class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        self.subset(target, nums, [], 0, res)
        return res

    def subset(self, target, nums, temp, l, res):
        if target < 0 or l>len(nums)-1:
            return
        elif target == 0:
            temp = sorted(temp,key = lambda x:x)
            if temp not in res:
                res.append(temp)
            return
        else:
            #for i in range(l,len(nums)):
            self.subset(target-nums[l], nums,temp+[nums[l]],l, res)
            self.subset(target,nums,temp,l+1, res)
                #self.subset(target-nums[i], nums,temp+[nums[i]],l, res)