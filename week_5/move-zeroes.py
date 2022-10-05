# https://leetcode.com/problems/move-zeroes/



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
                
        nums[i:] = [0] * (len(nums) - i)
