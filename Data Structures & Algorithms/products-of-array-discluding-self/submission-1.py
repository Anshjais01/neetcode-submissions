class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=[]
        n = len(nums)
        pro = [1] * n

        left = 1

        for i in range(n):
            pro[i] = left
            left *= nums[i]

        right = 1

        for i in range(n - 1, -1, -1):
            pro[i] *= right
            right *= nums[i]
        return pro
        


        