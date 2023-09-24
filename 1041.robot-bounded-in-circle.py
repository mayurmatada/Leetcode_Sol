#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        heading = "N"
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
                if(i == "L" and heading == "N"):
                    heading = "W"
                elif(i == "L" and heading == "E"):
                    heading = "N"
                elif(i == "L" and heading == "W"):
                    heading = "S"
                elif(i == "L" and heading == "S"):
                    heading = "E"
                elif(i == "R" and heading == "N"):
                    heading = "E"
                elif(i == "R" and heading == "E"):
                    heading = "S"
                elif(i == "R" and heading == "W"):
                    heading = "N"
                elif(i == "R" and heading == "S"):
                    heading = "W"

        while(heading != "N"):
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
                    if(i == "L" and heading == "N"):
                        heading = "W"
                    elif(i == "L" and heading == "E"):
                        heading = "N"
                    elif(i == "L" and heading == "W"):
                        heading = "S"
                    elif(i == "L" and heading == "S"):
                        heading = "E"
                    elif(i == "R" and heading == "N"):
                        heading = "E"
                    elif(i == "R" and heading == "E"):
                        heading = "S"
                    elif(i == "R" and heading == "W"):
                        heading = "N"
                    elif(i == "R" and heading == "S"):
                        heading = "W"
                    

        return True if Pos == [0,0] else False
# @lc code=end

