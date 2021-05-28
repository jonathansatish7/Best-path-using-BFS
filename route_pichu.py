#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : [Name: Jonathan Satish Tirupuranthakam, Username:josatiru]
#
# Based on skeleton code provided in CSCI B551, Spring 2021.


import sys
import json

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().rstrip("\n").split("\n")]


# Return a string with the board rendered in a human/pichu-readable format
def printable_board(board):
    return "\n".join(["".join(row) for row in board])


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
def moves(map, row, col, dir_str):
    #included the path string for getting path along with the co-ordinates
    moves = ((row + 1, col,dir_str+'D'), (row - 1, col,dir_str+'U'), (row, col - 1,dir_str+'L'), (row, col + 1,dir_str+'R'))
    #print(moves)
    # Return only moves that are within the board and legal (i.e. go through open space ".")
    return [move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)
#
def search(house_map):
    # Find pichu start position
    pichu_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if
                 house_map[row_i][col_i] == "p"][0]
    '''my_loc = [(row_i, col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if
                 house_map[row_i][col_i] == "@"][0]
    if not my_loc:
        return (-1,'')'''
    #print(pichu_loc)
    #print(my_loc)
    #included empty string for getting the path of pichu
    fringe = [(pichu_loc, 0,'')]
    #L = []
    #the below list has all the visited nodes to avoid revisiting them
    visited=[]
    while fringe:
        (curr_move, curr_dist,dir) = fringe.pop()
        visited.append(curr_move)
        #print(curr_move,curr_dist,dir)
        #L.append([curr_move,curr_dist])
        #flag='Y'
        for move in moves(house_map, *curr_move,dir):
            if house_map[move[0]][move[1]] == "@":
                #flag='Y'
                '''a=0
                L1=[]
                str=""
                for i in range(0,len(L)):
                    if L[i][1]==a+1:
                        L1.append(L[i-1][0])
                        a=a+1
                L1.append(L[len(L)-1][0])
                print(L1)
                for i in range(0,len(L1)-1):
                    if L1[i][0]-L1[i+1][0]==1:
                        str=str+'U'
                    elif L1[i][0]-L1[i+1][0]==-1:
                        str=str+'D'
                    elif L1[i][1]-L1[i+1][1]==-1:
                        str=str+'R'
                    else:
                        str=str+'L' '''
                #returning the curr_dist+1 as it is not including final move to @
                return (curr_dist+1, move[2])  # return a dummy answer
            else:
                if move[0:2] not in visited:
                    fringe.insert(0,(move[0:2], curr_dist + 1,move[2]))
                    #flag='N'
    #returns below if it can't find the path
    return(-1,'')


# Main Function
if __name__ == "__main__":
    house_map = parse_map(sys.argv[1])
    print("Routing in this board:\n" + printable_board(house_map) + "\n")
    print("Shhhh... quiet while I navigate!")
    solution = search(house_map)
    print("Here's the solution I found:")
    print(str(solution[0]) + " " + str(solution[1]))
