class Solution:
    def search(self, nums: List[int], target: int) -> int:
        val=0
        if target in nums:
            val=nums.index(target)
        else:
            val=-1
        return val
        