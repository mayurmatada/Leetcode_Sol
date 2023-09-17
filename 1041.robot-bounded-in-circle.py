#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        heading = "N"
        directions = ['N', 'E', 'S', 'W']
        Pos = [0,0]
        for i in instructions:
            if(i == "G"):
                if(heading == "N"):
                    Pos[1] += 1
                if(heading == "E"):
                    Pos[0] += 1
                if(heading == "W"):
                    Pos[0] -= 1
                if(heading == "S"):
                    Pos[1] -= 1
            else:
                if(i == "L" and heading != 'N'):
                    heading = directions[directions.index(heading)-1]
                elif(i == "R" and heading != 'W'):
                    heading = directions[directions.index(heading)+1]
                elif(i == "R" and heading == 'W'):
                    heading = "N"
                if(i == "L" and heading == 'N'):
                    heading = "W"
        return True if Pos == [0,0] else False
# @lc code=end

