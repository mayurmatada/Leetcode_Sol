from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)/2
        counts = {}

        for i in nums:
            if (counts[i] == None):
                counts[i] = 1
            else:
                counts[i] += 1

        for k, v in counts.items():
            if (v > n/2):
                return k
