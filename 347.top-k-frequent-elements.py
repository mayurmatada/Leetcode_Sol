#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = list(set(nums))
        counter = {}
        result = []
        for i in unique:
            try:
                counter[nums.count(i)].append(i)
            except:
                counter[nums.count(i)] = [i]
        counter_list = list(counter.keys())
        counter_list.sort()
        for j in range(-1, -len(counter_list)-1, -1):
            try:
                for f in counter[counter_list[j]]:
                    result.append(f)
            except: pass
        return result[0:k]


# @lc code=end

