from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    #Check rows
    counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in board:
        for j in i:
            if (ord(j)-48) in counter:
                counter[int(j)] += 1
        for k in counter.values():
            if(k > 1):
                return False
        counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        
    #Check columns    
    counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    c = []
    for l in range(0,9):
        for b in range(0,9):
            c.append(board[b][l])
        for m in c:
            if (ord(m)-48) in counter:
                counter[int(m)] += 1
        for n in counter.values():
            if(n > 1):
                return False
        counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        c = []
        
    #Check squares
    counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    c= []
    cur = [0,0]
    for y in range(0,3):
        for h in range(0, 3):
            for p in range(cur[0], cur[0]+3):
                for q in range(cur[1], cur[1]+3):
                    c.append(board[p][q])
                    
            for s in c:
                if (ord(s)-48) in counter:
                            counter[int(s)] += 1
            for t in counter.values():
                if(t > 1):
                    return False
            counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
            c=[]
            cur [0] += 3
        cur[1] += 3
        cur[0] = 0
        
    
    return True


print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    ,["6",".",".","1","9","5",".",".","."]
                    ,[".","9","8",".",".",".",".","6","."]
                    ,["8",".",".",".","6",".",".",".","3"]
                    ,["4",".",".","8",".","3",".",".","1"]
                    ,["7",".",".",".","2",".",".",".","6"]
                    ,[".","6",".",".",".",".","2","8","."]
                    ,[".",".",".","4","1","9","7",".","5"]
                    ,[".",".",".",".","8",".",".","7","9"]]))