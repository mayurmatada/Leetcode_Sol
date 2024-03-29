#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areasRL = [[]]
        cur = 0
        for i in heights[::-1]:
            if(areasRL[cur] == []):
                areasRL[cur].append(i)
                continue
            elif(((len(areasRL[cur])*sorted(areasRL[cur])[0]) <= (len(areasRL[cur])+1)*i) and (i <= areasRL[cur][-1])):
                areasRL[cur].append(i)
            else:
                cur += 1
                areasRL.append([])
                areasRL[cur].append(i)
        areasLR = [[]]
        cur = 0
        for i in heights:
            if(areasLR[cur] == []):
                areasLR[cur].append(i)
                continue
            elif(((len(areasLR[cur])*sorted(areasLR[cur])[0]) <= (len(areasLR[cur])+1)*i) and (i >= areasLR[cur][-1]) and i != 0):
                areasLR[cur].append(i)
            else:
                cur += 1
                areasLR.append([])
                if(i != 0):
                    areasLR[cur].append(i)
        prod = []
        areas = areasLR + areasRL
        for k in areas:
            prod.append(sorted(k)[0]*len(k))
        
        return sorted(prod)[-1]
            
        
# @lc code=end

