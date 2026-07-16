class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * len(nums)
        prefix = [1] * len(nums)
        for i in range(len(nums)):
            prev_prefix = prefix[i - 1] if i > 0 else 1
            prev_num = nums[i - 1] if i > 0 else 1
            prefix[i] = prev_prefix * prev_num
        for i in range(len(nums) - 1, -1, -1):
            print(i)
            next_suffix = suffix[i + 1] if i < len(nums) - 1 else 1
            next_num = nums[i + 1] if i < len(nums) - 1 else 1
            suffix[i] = next_suffix * next_num
        result = []   
        for i in range(len(nums)):
            result.append(suffix[i] * prefix[i])
        return result
        