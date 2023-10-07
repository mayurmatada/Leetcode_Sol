#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if(i != "+" and i != "-" and i != "*" and i != "/"):
                stack.append(int(i))
            else:
                if(i == "+"):
                    res = stack[-2] + stack[-1]
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(res)
                elif(i == "-"):
                    res = stack[-2] - stack[-1]
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(res)
                elif(i == "*"):
                    res = stack[-2] * stack[-1]
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(res)
                elif(i == "/"):
                    res = int(stack[-2] / stack[-1])
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(res)
        return stack[0]
# @lc code=end

