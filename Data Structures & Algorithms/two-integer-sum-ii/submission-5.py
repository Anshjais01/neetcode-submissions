class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers=sorted(numbers)
        l,r=0,len(numbers)-1
        while l<r:
            pres_sum=numbers[l]+numbers[r]

            if pres_sum>target:
                r-=1
            elif pres_sum<target:
                l+=1
            else:
                return [l+1,r+1]


            