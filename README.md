# Name: Jonathan Satish Tirupuranthakam
# Username: josatiru 

# Part1: Navigation

1. So in the start I have gone through the code route_pichu and I have placed several print statements "print(curr_move,curr_dist,dir)" and "print(moves)" in order to know what are getting inserted into the fringe and popped out of fringe.
2. Then realized that the all the elements are not going into the fringe and then as the search function is using stack (appending to the end and popping from end). So it was implementing the DFS which is incomplete and it's not verifying all the possibilities and then I modified the stack to queue by popping from the last and then inserting in the beginning of the list by using "fringe.insert(0,(move[0:2], curr_dist + 1,move[2]))".
3. After the above modification I was able to get the number of moves correctly but it was one less than the required count and then I realized that the last move from . to @ is not being considered and then I added the remaining move it then returned the correct value.
4. Now I had to figure out a way to print the direction pichu has to follow in order to reach @. So I started printing out the items which are being popped out of fringe that has the co-ordinates of the pichu and also the number of moves pichu already made. which is of this format
- (5, 0) 0
- (4, 0) 1 U
- (3, 0) 2 UU
- (2, 0) 3 UUU
- (1, 0) 4 UUUU
- (2, 1) 4 UUUR
- (0, 0) 5 UUUUU
- (2, 2) 5 UUURR
- (0, 1) 6 UUUUUR
- (3, 2) 6 UUURRD
- (2, 3) 6 UUURRR
- (0, 2) 7 UUUUURR
- (4, 2) 7 UUURRDD
- (0, 3) 8 UUUUURRR

and then I checked on some co-ordinates and observed that last co-ordinate of the same number of moves was giving correct direction, if suppose we consider number of directions as 4 then there are two co-ordinates from the above list ((1,0),(2,1)). I will take the latest co-ordinate which has the number of moves as 4 and then insert in a empty list and I did the same for the entire thing.

5. After moving all the valid items to the List I compared the every two elements in the list so that I get the direction in which pichu has to move.

                a=0
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
                        str=str+'L'

6. But I realised that this method won't help me as the procedure is not true always and I got wrong path and then thought I would include the direction in the moves function itself so the direction will be computed parallelly along with the co-ordinates and the number of moves. I created an empty string and inserted in the first element in the fringe along with pichu primary location and the 0 as pichu didn't make any move yet

fringe = [(pichu_loc, 0,'')]

7. Then it returned the correct path that pichu has to follow in order to reach the destination.

8. But when I gave a map where there is no route my program wasn't terminating, then I again printed the elements which are entering the fringe and the items which are getting popped out of fringe and I found the already visited nodes are being revisited and it going in infinite loop.

9. Then I tried to assign Flag to the nodes which are popped out of the fringe but this method didn't work out and I then tried inserting all the popped out elements from the fringe to a empty list.

visited=[]
    while fringe:
        (curr_move, curr_dist,dir) = fringe.pop()
        visited.append(curr_move)

Then I only append the elements into the fringe which are not in the visited node

if move[0:2] not in visited:
    fringe.insert(0,(move[0:2], curr_dist + 1,move[2]))

10. Then all the issues were solved and I got the correct path and the number of moves the pichu takes to reach the destination. After I eliminated the revisiting of already visited nodes my program ran quickly than before.


* The set of valid states are: The next move which has '.' and '@' will be considered as valid state and the next move with 'X' will be considered as invalid state.

* The successor function: The function will be that the pichu should always make a move where there is '.' we should not make a move towards 'X' till we reach the destination at '@' with minimum number of moves. In this case it is moves function
def moves(map, row, col, dir_str):

* There is no cost function in this case.

* In this case the goal state will be the the destination tile that is '@' so if the pichu arrives at this tile successfully we can say that pichu has achieved the goal.

* The initial state will be the initial location of the pichu. so, in this case the initial location will be 'p'.




# Part2: Hide and Seek

1. In this part we will be working on arranging the pichus 'p' such that no pichu will be on the same row and columnn until or unless there is an obstacle in between pichus. The obstacle can either be the wall 'X' or the person '@'.

2. Like the previous part the first thing I did is that I used the print statements to understand what is entering the fringe and what are getting popped out of the fringe.  

3. The successors function in this case prints out all the possible successors to the initial state which is the initial board setup. The successors function uses the add_pichu method and prints out all the possible successors in the below format

[['p', '.', '.', '.', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', '.', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.'], ['.', 'X', '.', 'X', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.'], ['p', 'X', '.', '.', '.', 'X', '@']]
[['.', 'p', '.', '.', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', '.', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.'], ['.', 'X', '.', 'X', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.'], ['p', 'X', '.', '.', '.', 'X', '@']]
[['.', '.', 'p', '.', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', '.', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.'], ['.', 'X', '.', 'X', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.'], ['p', 'X', '.', '.', '.', 'X', '@']]
[['.', '.', '.', 'p', 'X', 'X', 'X'], ['.', 'X', 'X', 'X', '.', '.', '.'], ['.', '.', '.', '.', 'X', '.', '.'], ['.', 'X', '.', 'X', '.', '.', '.'], ['.', 'X', '.', 'X', '.', 'X', '.'], ['p', 'X', '.', '.', '.', 'X', '@']]

4. So if we look at the above case all the possibilities are being passed on to the fringe even though they are invalid state. initially so in order to eliminate the invalid cases being pushed into the fringe I have defined some set of conditions in the check_before_append function

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

The above conditions checks for all 'p' on the map on the directions (Up, Down, Left and Right) from the point 'p', if one more 'p' appears before 'X' or '@' The function will return False stating that it is invalid condition and it won't add in the fringe.

5. The is_goal function checks whether the map has number of 'p' which are required then it would return the map and the whole program terminates, but when I directly returned and it throws wrong map as it calls all successors of popped out item in fringe so in order to avoid this we have verify the all the successors using the previous condition.

6. Then I printed the whole fringe and verified. Then I found that there are again invalid states even though they are valid before entering into fringe.

7. I then eliminated the invalid state by including the same condition mentioned above and then ran the program and I got the required map.


* The set of valid states in this problem is the map which has 'p' in such a form that no two 'p' are on the same row and same column until or unless there is wall or man between them.

* The successor function is the function which generates the next map by adding pichus, in this case the successor function is
def successors(board):
    return [ add_pichu(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' ] returns all the

* There is no cost function in this case.

* In this case the goal state will be the map with required number of pichus where no pichu can see each other.

* The initial state will be map which we enter before the program runs.
