class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prev_prefix = result[i - 1] if i > 0 else 1
            prev_num = nums[i - 1] if i > 0 else 1
            result.append(prev_prefix * prev_num)
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]
        return result