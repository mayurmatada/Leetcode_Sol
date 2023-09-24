#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        pos = [1,1]
        heading = 2
        rows = len(matrix)
        columns = len(matrix[0])

        #Upper and lower padding
        matrix.append(["X" for i in range(0, columns+1)])
        matrix.reverse()
        matrix.append(["X" for i in range(0, columns+1)])
        matrix.reverse()

        #Side padding
        for i in range(1, rows+1):
            matrix[i].append("X")
            matrix[i].reverse()
            matrix[i].append("X")
            matrix[i].reverse()

        #Cursor
        while(len(result) != rows*columns):
            result.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = "X"

            #Movement
            if(heading == 1):
                if(matrix[pos[0]-1][pos[1]] != "X"):
                    pos[0] = pos[0]-1
                else:
                    heading = 2
                    pos[1] = pos[1]+1
            elif(heading == 2):
                if(matrix[pos[0]][pos[1]+1] != "X"):
                    pos[1] = pos[1]+1
                else:
                    heading = 3
                    pos[0] = pos[0]+1
            elif(heading == 3):
                if(matrix[pos[0]+1][pos[1]] != "X"):
                    pos[0] = pos[0]+1
                else:
                    heading = 4
                    pos[1] = pos[1]-1
            elif(heading == 4):
                if(matrix[pos[0]][pos[1]-1] != "X"):
                    pos[1] = pos[1]-1
                else:
                    heading = 1
                    pos[0] = pos[0]-1

        return result
    
    

    
        
            


            



# @lc code=end

