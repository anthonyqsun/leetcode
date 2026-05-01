class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        def rotate_generator(k, n):
            for i in range(n):
                j = (i+n-k) % n
                yield nums[j]
            return

        out = float("-inf")
        n = len(nums)
        for k in range(n):
            arrk = rotate_generator(k, n)
            F = 0
            for i in range(n):
                F += i * next(arrk)
            out = max(out, F)
        return out
