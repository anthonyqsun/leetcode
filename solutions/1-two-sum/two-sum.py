class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            if (ti := map.get(target-n)) is not None:
                return [i, ti]
            map[n] = i
        return None