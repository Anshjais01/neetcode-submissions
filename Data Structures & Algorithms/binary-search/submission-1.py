class Solution:
    def search(self, nums: List[int], target: int) -> int:
        val=0
        if target in nums:
            val=nums.index(target)
        else:
            val=-1
        return val
        
        
        # mid=len(nums)//2
        # if target not in nums:
        #     mid=-1
        # return mid
        # else:
        #     if nums[mid]>target:
        #         mid-=1
        #     elif nums[mid]<target:
        #         mid+=1
            
        #     return mid
            
        
        