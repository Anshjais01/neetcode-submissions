class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        lst=set(nums)
        for num in lst:
            if num-1 not in lst:
                count=1
            
                while num+count in lst:
                    count+=1
        
                longest= max(longest,count)

        return longest
            



        