class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count[num] + 1 if num in count else 1
        track = [None] * (len(nums) + 1)
        
        for num in count:
            if track[count[num]] is None:
                track[count[num]] = []    
            track[count[num]].append(num)

        result = []
        remaining = k
        i = len(track) - 1
        while remaining > 0:
            if track[i] is not None:
                result = result + track[i][0:remaining]
                remaining = remaining - len(track[i])
            i = i - 1
        return result