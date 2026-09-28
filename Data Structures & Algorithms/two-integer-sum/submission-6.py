class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        get=[]
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in nums[i+1:]:
                get.append(i)
                get.append(nums[i+1:].index(sub) + (i + 1))
                break
        return get
                
        