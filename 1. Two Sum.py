from Typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)  # Get the length of the input list
        for i in range(len(nums)):  # Iterate through each index in the list
            try:
                # Find the index of the complement of the current number in the remaining sublist
                index = nums.index(target - nums[i], i + 1, n)
                return [i, index]  # Return the indices of the two numbers that sum up to the target
            except:
                pass  # Ignore any exceptions and continue the loop
