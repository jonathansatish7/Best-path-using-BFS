#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [Name: Jonathan Satish Tirupuranthakam, Username: josatiru]
#
# Based on skeleton code in CSCI B551, Spring 2021
#


import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]

# Count total # of pichus on board
def count_pichus(board):
    return sum([ row.count('p') for row in board ] )

# Return a string with the board rendered in a human-pichuly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a pichu to the board at the given position, and return a new board (doesn't change original)
def add_pichu(board, row, col):
    #print(board[0:row] + [board[row][0:col] + ['p',] + board[row][col+1:]] + board[row+1:])
    return board[0:row] + [board[row][0:col] + ['p',] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' ]

# check if board is a goal state and checks whether the successor of the popped out element of fringe is valid
def is_goal(board, k):
    if count_pichus(board)==k:
        #print(k)
        for row in range(0,len(board)):
            for column in range(0,len(board[0])):
                if(board[row][column]=='p'):
                    for i in range(row+1,len(board)):
                        if board[i][column]=='X' or board[i][column]=='@':
                            break
                        if board[i][column]=='p':
                            return False
                    for i in range(row-1,-1,-1):
                        if board[i][column]=='X' or board[i][column]=='@':
                            break
                        if board[i][column]=='p':
                            return False
                    for i in range(column+1,len(board[0])):
                        if board[row][i]=='X' or board[row][i]=='@':
                            break
                        if board[row][i]=='p':
                            return False
                    for i in range(column-1,-1,-1):
                        if board[row][i]=='X' or board[row][i]=='@':
                            break
                        if board[row][i]=='p':
                            return False
        return True
    else:
        return False

#Checks all the states whether they are valid or not before inserting in the fringe
def check_before_append(board):
    for row in range(0,len(board)):
        for column in range(0,len(board[0])):
            if(board[row][column]=='p'):
                for i in range(row+1,len(board)):
                    if board[i][column]=='X' or board[i][column]=='@':
                        break
                    if board[i][column]=='p':
                        return False
                for i in range(row-1,-1,-1):
                    if board[i][column]=='X' or board[i][column]=='@':
                        break
                    if board[i][column]=='p':
                        return False
                for i in range(column+1,len(board[0])):
                    if board[row][i]=='X' or board[row][i]=='@':
                        break
                    if board[row][i]=='p':
                        return False
                for i in range(column-1,-1,-1):
                    if board[row][i]=='X' or board[row][i]=='@':
                        break
                    if board[row][i]=='p':
                        return False
    return True

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_map, success), where:
# - new_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_board, k):
    fringe = [initial_board]
    #the below list has the already visited states
    visited=[]
    while len(fringe) > 0:
        a=fringe.pop()
        #print('\n')
        #print(a)
        visited.append(a)
        #print('\n')
        for s in successors(a):
            #print(s)
            if is_goal(s, k)==True:
                return(s,True)
            if check_before_append(s)==True and s not in visited:
                fringe.append(s)
        #print(fringe)
    return ([],False)



# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])

    # This is K, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(house_map) + "\n\nLooking for solution...\n")
    (newboard, success) = solve(house_map, k)
    print ("Here's what we found:")
    print (printable_board(newboard) if success else "None")


