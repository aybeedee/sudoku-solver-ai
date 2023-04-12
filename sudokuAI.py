puzzle = [
    [5, 0, 2, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 1, 0, 5],
    [0, 7, 0, 2, 0, 0, 0, 5, 0],
    [8, 9, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 4, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [1, 5, 6, 9, 0, 0, 0, 0, 0]
]

puzzle1 = [
    [5, 0, 2, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 1, 0, 5],
    [0, 7, 0, 2, 0, 0, 0, 5, 0],
    [8, 9, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 4, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [1, 5, 6, 9, 0, 0, 0, 0, 0]
]

temp = [
    [0, 6, 0, 1, 0, 4, 0, 5, 0],
    [0, 0, 8, 3, 0, 5, 6, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [8, 0, 0, 4, 0, 7, 0, 0, 6],
    [0, 0, 6, 0, 0, 0, 3, 0, 0],
    [7, 0, 0, 9, 0, 1, 0, 0, 4],
    [5, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 7, 2, 0, 6, 9, 0, 0],
    [0, 4, 0, 5, 0, 8, 0, 7, 0]
]

def printPuzzle(sudokuBoard):
    
    for i in range(9):
        
        print("\n")
        
        for j in range(9):
            
            print(" | ", sudokuBoard[i][j], end = "")
            
printPuzzle(puzzle)

def displayMRVList(mrv_list):
    
    for i in range(len(mrv_list)):
        
        print(i, ": ", mrv_list[i])

def getBox(row, col):
    
    if (row >= 0) and (row <= 2):
        
        if (col >= 0) and (col <= 2):
            
            return [0,0]

        elif (col >= 3) and (col <= 5):
            
            return [0,3]
        
        else:
        
            return [0,6]
        
    elif (row >= 3) and (row <= 5):
        
        if (col >= 0) and (col <= 2):
            
            return [3,0]

        elif (col >= 3) and (col <= 5):
            
            return [3,3]
        
        else:
        
            return [3,6]
        
    else:
        
        if (col >= 0) and (col <= 2):
            
            return [6,0]

        elif (col >= 3) and (col <= 5):
            
            return [6,3]
        
        else:
        
            return [6,6]

def findSmallestDomain(blankCells):
    
    minRemValues = 10
    index = 0
    
    for i in range(len(blankCells)):
    
        if (not blankCells[i][0]):
    
            if (len(blankCells[i][3]) <= minRemValues):

                minRemValues = len(blankCells[i][3])
                index = i
            
    return [minRemValues, index]

def allAssigned(blankCells):
    
    for i in range(len(blankCells)):
        
        if (blankCells[i][0] == False):
            
            return False
        
    return True

MRVList = []

for i in range(9):
    
    for j in range(9):
        
        if (puzzle[i][j] == 0):
            
            tempList = [1,2,3,4,5,6,7,8,9]
        
            for k in range(9):
                
                if (k == j):
                    
                    continue
                    
                if (puzzle[i][k] in tempList):
                
                    tempList.remove(puzzle[i][k])
            
            for l in range(9):
                
                if (k == i):
                    
                    continue
                    
                if (puzzle[l][j] in tempList):
                    
                    tempList.remove(puzzle[l][j])
                    
            boxStart = getBox(i,j)
            
            boxCheckInd1 = boxStart[0]
            boxCheckInd2 = boxStart[1]
            
            for m in range (boxCheckInd1, (boxCheckInd1+3)):
                
                for n in range (boxCheckInd2, (boxCheckInd2+3)):
                    
                    if ((m == i) and (n == j)):
                        
                        continue
                    
                    if (puzzle[m][n] in tempList):
                        
                        tempList.remove(puzzle[m][n])
            
            blankMRV = [
                
                False,
                0,
                [i,j],
                tempList,
                [],
                []
            ]
            
            MRVList.append(blankMRV)

displayMRVList(MRVList)

#stack for backtracking with forward checking
stack = []

#list for storing solutions where only one possible value is left and is causing infinite loops
visited = []

#keep iterating until all blank cells successfully assigned
while (not allAssigned(MRVList)):
#for x in range(100):
    
    displayMRVList(MRVList)
    print()
    
    #find the next blank to fill using MRV
    [minRemValues, index] = findSmallestDomain(MRVList)
    
    print("index: ", index, "\n", "mrvs: ", minRemValues)
    
    #if the min is 0, it means we have to terminate search in this path as a cell exists that has no legal values
    if (minRemValues == 0):
        
        #backtrack
        ind = stack.pop()
        
        #print("\n", index, " VISITED ", ind, "\n")
        
        #if remaining values list is empty then readd and cause next value in stack to be popped
        if (len(MRVList[ind][3]) == 0):
            
            MRVList[ind][0] = False
            MRVList[ind][1] = 0
            
            for c in range(len(MRVList[ind][5])):
                
                MRVList[ind][3].append(MRVList[ind][5][c][0])
                
                
            MRVList[ind][5] = []
            rowCol2 = MRVList[ind][2]
            
            for f in range(len(MRVList[ind][4])):
                
                temp = MRVList[ind][4][f]
                MRVList[ind][3].append(temp)
                MRVList[ind][4].remove(temp)
                
                #remove all constraints caused by respective value
                for d in range(len(MRVList)):
                        
                    if (ind == d):
                            
                        continue
                            
                    if ([temp, rowCol2] in MRVList[d][5]):
                            
                        MRVList[d][5].remove([temp, rowCol2])
                        MRVList[d][3].append(temp)
                        
            #[minRemValues, index] = findSmallestDomain(MRVList)
        
        else:
            
            #on this index, undo assignment and add back all the domain removals from constrained cells
            # + add new domain constraints
            for g in range(len(MRVList[ind][3])):

                if (MRVList[ind][3][g] not in MRVList[ind][4]):

                    newVal = MRVList[ind][3][g]
                    prevVal = MRVList[ind][1]
                    MRVList[ind][1] = newVal
                    MRVList[ind][3].remove(newVal)
                    MRVList[ind][4].append(newVal)
                    rowCol = MRVList[ind][2]
                    
                    #remove all constraints caused by last value
                    for e in range(len(MRVList)):
                        
                        if (ind == e):
                            
                            continue
                            
                        if ([prevVal, rowCol] in MRVList[e][5]):
                            
                            MRVList[e][5].remove([prevVal, rowCol])
                            MRVList[e][3].append(prevVal)
                            
                    
                    break

            stack.append(ind)
            
            #[minRemValues, index] = findSmallestDomain(MRVList)
        
    else:
        
        #push that index to stack
        stack.append(index)
        
        #set the value to next possible value in it's legal domain
        possibleVal = 0
        
        for h in range(len(MRVList[index][3])):
            
            if (MRVList[index][3][h] not in MRVList[index][4]):
                
                possibleVal = MRVList[index][3][h]
                MRVList[index][1] = possibleVal
                MRVList[index][3].remove(possibleVal)
                MRVList[index][4].append(possibleVal)
                MRVList[index][0] = True
                
                break
        
        indices = MRVList[index][2] 
        
        boxStart = getBox(indices[0], indices[1])
        
        boxCheckInd1 = boxStart[0]
        boxCheckInd2 = boxStart[1]
        
        #remove the assigned value from all cells that are constrained by present cell
        for i in range(len(MRVList)):
            
            #if not already assigned, alter domain
            if (not MRVList[i][0]):
                
                #if same row or same column
                if ((MRVList[i][2][0] == indices[0]) or (MRVList[i][2][1] == indices[1])):
                    
                    if (possibleVal in MRVList[i][3]):
                        
                        MRVList[i][3].remove(possibleVal)
                        MRVList[i][5].append([possibleVal, indices])
                        
                #if same box
                for j in range (boxCheckInd1, (boxCheckInd1+3)):
                
                    for k in range (boxCheckInd2, (boxCheckInd2+3)):
                    
                        if ((j == indices[0]) and (k == indices[1])):
                        
                            continue
                    
                        if (MRVList[i][2] == [j, k]):
                    
                            if (possibleVal in MRVList[i][3]):

                                MRVList[i][3].remove(possibleVal)
                                MRVList[i][5].append([possibleVal, indices])
                
for i in range(len(MRVList)):
    
    [row, col] = MRVList[i][2]
    val = MRVList[i][1]
    
    puzzle[row][col] = val

printPuzzle(puzzle)

#MRV LIST STRUCTURE:
"""[
    [
        0 assignment status : assignedBool,
        1 assigned value: 0,
        2 index: [row, col],
        3 values remaining: [1,3,4,5,6,8],
        
        4 values explored: [],
        
        5 values removed due to domain constraint of other assignments:
        [
            [2, [1,2]],
            [7, [4,6]],
            [9, [0,0]]
        ]
    ]
    
]"""