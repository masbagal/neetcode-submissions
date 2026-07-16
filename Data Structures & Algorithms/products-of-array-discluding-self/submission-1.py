class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(len(nums)):
            prev_prefix = result[i - 1] if i > 0 else 1
            prev_num = nums[i - 1] if i > 0 else 1
            result[i] = prev_prefix * prev_num
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]

        return result